# Webhooks - URL Shortener

A URL shortener that progressively adds webhook support across three versions.

## v1 - Plain URL Shortener

No webhooks. Just the core short-link domain.

### Run

```bash
cd v1
uvicorn main:app --reload --port 8000
```

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST /links` | Create a short link |
| `GET /links` | List all short links |
| `GET /{short_code}` | Redirect to target URL (increments clicks) |

### Test

Create a short link:

```bash
curl -X POST http://localhost:8000/links \
  -H "Content-Type: application/json" \
  -d '{"target_url": "https://www.arjancodes.com"}'
```

List all links:

```bash
curl http://localhost:8000/links
```

Click a short link (replace `<short_code>` from create response):

```bash
curl -L http://localhost:8000/<short_code>
```

List again to see clicks incremented:

```bash
curl http://localhost:8000/links
```

## v2 - Direct Webhook Delivery

v1 had no way to notify external systems when things happen. Consumers would need to poll `GET /links` constantly. Webhooks solve this: "don't call us, we'll call you."

v2 lets consumers register a callback URL. When a link is created or clicked, the app POSTs a JSON payload to every registered URL.

### What Changed from v1

**New file: `webhooks.py`** — manages webhook registration and delivery:
- `Webhook` model — just an `id` and `url`
- `POST /webhooks` — register a URL to receive callbacks
- `GET /webhooks` — list registered webhooks
- `send_webhooks(data)` — loops through all registered webhooks and POSTs the payload via `httpx`
- `deliver_webhook(webhook, data)` — the actual HTTP POST with a 5-second timeout

**Modified: `links.py`** — now imports `send_webhooks` and calls it in two places:
1. `create_short_link` — after creating a link, builds a `link.created` payload and calls `send_webhooks()`
2. `redirect_to_target` — after incrementing clicks, builds a `link.clicked` payload and calls `send_webhooks()`

### The Problem

`links.py` is now doing two jobs:
1. Managing short links (its actual job)
2. Knowing what webhook payload to build and calling the webhook system

Every field in the payload dict is hand-constructed inside the endpoint. If you add a new feature (say, "link deleted"), you'd add more webhook code right there. If you add a second notification channel (email, Slack), `links.py` has to know about that too. This is **tight coupling** — the thing that emits events knows about every consumer of those events.

v3 solves this with an event bus.

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST /links` | Create a short link (sends `link.created` webhook) |
| `GET /links` | List all short links |
| `GET /{short_code}` | Redirect to target URL (sends `link.clicked` webhook) |
| `POST /webhooks` | Register a webhook URL |
| `GET /webhooks` | List registered webhooks |

### Run

```bash
# Terminal 1: start the webhook receiver
uvicorn webhook_receiver:app --reload --port 9001

# Terminal 2: start v2
cd v2
uvicorn main:app --reload --port 8000
```

### Test

Register the receiver as a webhook:

```bash
curl -X POST http://localhost:8000/webhooks \
  -H "Content-Type: application/json" \
  -d '{"url": "http://localhost:9001/webhook"}'
```

Create a short link (triggers `link.created` webhook):

```bash
curl -X POST http://localhost:8000/links \
  -H "Content-Type: application/json" \
  -d '{"target_url": "https://www.arjancodes.com"}'
```

Click the short link (triggers `link.clicked` webhook):

```bash
curl -L http://localhost:8000/<short_code>
```

Check what the receiver got:

```bash
curl http://localhost:9001/webhooks
```

## v3 - Event Bus (Decoupled)

v2's problem: `links.py` directly imports and calls `send_webhooks()`. It builds the payload, knows about the webhook system, and would need to know about every future notification channel. The more events and consumers you add, the worse the coupling gets.

v3 introduces the **Observer pattern** via an `EventBus`:
- **Publishers** say "something happened" without caring who's listening
- **Subscribers** say "tell me when X happens" without caring who publishes it
- The **EventBus** sits in the middle and routes events to subscribers

### Architecture

```
                         main.py
                    creates & wires EventBus
                            |
              .configure()  |  .configure()
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
         ┌─────────┐  ┌──────────┐  ┌──────────────┐
         │ links.py │  │ EventBus │  │ webhooks.py  │
         │          │  │          │  │              │
         │ publish()├─►│ EventType│  │ subscribe()  │
         │          │  │ listeners├─►│              │
         └─────────┘  └──────────┘  └──────┬───────┘
                                           │ HTTP POST
                                           ▼
                                    ┌──────────────┐
                                    │   External   │
                                    │   Receiver   │
                                    └──────────────┘

  Adding a new publisher:          Adding a new subscriber:
  ┌──────────┐                     ┌──────────────┐
  │ users.py │──publish()──►       │  slack.py    │
  │          │             │       │              │
  └──────────┘       ┌─────┴────┐  │ subscribe()  │
                     │ EventBus │──►              │
                     └─────┬────┘  └──────────────┘
                           │       ┌──────────────┐
                           │       │  email.py    │
                           └──────►│ subscribe()  │
                                   └──────────────┘
  No changes needed to existing publishers or subscribers!
```

### What Changed from v2

**New file: `events.py`** — the decoupling layer:
- `EventType` — a `StrEnum` defining `link.created` and `link.clicked`. The shared vocabulary between publishers and subscribers.
- `Event` — a Pydantic model wrapping every event with an `id`, `type`, `occurred_at` timestamp, and `data` dict.
- `EventBus` — the hub. A dict mapping each `EventType` to a list of listener callbacks.
  - `subscribe(event_type, listener)` — registers a callback for an event type
  - `publish(event_type, data)` — creates an `Event` object and calls every registered listener

**Modified: `links.py`** — no longer imports anything from webhooks. Just calls `event_bus.publish(EventType.LINK_CREATED, {...})`. Doesn't know or care if webhooks, email, Slack, or nothing is listening.

**Modified: `webhooks.py`** — no longer exposes `send_webhooks()`. Instead:
- Webhooks now have an `events` field — you choose *which* event types a webhook receives
- `attach_webhook_listener()` subscribes to the event bus for each event type the webhook cares about
- The delivery function receives a full `Event` object instead of a raw dict

**Modified: `main.py`** — creates the `EventBus` and wires everything:
- `links.configure(event_bus)` — gives links its publisher
- `webhooks.configure(event_bus)` — gives webhooks its subscriber

### Why This Is Better

- `links.py` and `webhooks.py` don't import each other
- Adding a new consumer (e.g. Slack notifications) means a new module that subscribes to the bus — zero changes to `links.py`
- Adding a new event type (e.g. `link.deleted`) means adding it to `EventType` and publishing it — zero changes to `webhooks.py`
- Webhook consumers can filter by event type instead of receiving everything

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST /links` | Create a short link (publishes `link.created` event) |
| `GET /links` | List all short links |
| `GET /{short_code}` | Redirect to target URL (publishes `link.clicked` event) |
| `POST /webhooks` | Register a webhook with event filtering |
| `GET /webhooks` | List registered webhooks |

### Run

```bash
# Terminal 1: start the webhook receiver
uvicorn webhook_receiver:app --reload --port 9001

# Terminal 2: start v3
cd v3
uvicorn main:app --reload --port 8000
```

### Test

Register a webhook that only listens to `link.clicked`:

```bash
curl -X POST http://localhost:8000/webhooks \
  -H "Content-Type: application/json" \
  -d '{
    "url": "http://localhost:9001/webhook",
    "events": ["link.clicked"]
  }'
```

Create a short link (receiver gets **nothing** — webhook didn't subscribe to `link.created`):

```bash
curl -X POST http://localhost:8000/links \
  -H "Content-Type: application/json" \
  -d '{"target_url": "https://www.arjancodes.com"}'
```

Click the short link (receiver **gets the event**):

```bash
curl -L http://localhost:8000/<short_code>
```

Register a webhook for both events:

```bash
curl -X POST http://localhost:8000/webhooks \
  -H "Content-Type: application/json" \
  -d '{
    "url": "http://localhost:9001/webhook",
    "events": ["link.created", "link.clicked"]
  }'
```

Create another link — this time the receiver gets the `link.created` event too.

Check everything the receiver got:

```bash
curl http://localhost:9001/webhooks
```

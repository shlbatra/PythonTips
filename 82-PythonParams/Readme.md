## Similar Params used across lot of methods and keep growing as code grows with new functionalities
1. Use keyword args but still methods require many arg variations so not solve underlying issue of params growing and also shared across different methods
# How to solve
1. Group data that pass around in a common object -> dataclass ex. VideoSearchQuery -> add all args, just pass VideoSearchQuery arg to all methods and simplify
2. Include validation at data class level next instead of method

---

## Code walk-through: `before.py`

`before.py` works correctly but deliberately shows a **parameter-passing smell**.

### Setup
- `SortOrder` / `Duration` are `Literal` type aliases that restrict certain args to a fixed set of string values.
- `Video` is a `@dataclass(frozen=True)` — an immutable value object that flows through the search pipeline.

### The smell: `search_videos` (9 parameters)
`search_videos` takes 9 parameters (`query, category, sort_by, upload_date, duration, region, include_shorts, max_results, language`) and then **re-threads those same params by hand** into every helper:
- `validate_search(...)` → 8 of them
- `get_cache_key(...)` → 8 of them
- `build_search_query(...)` → all 9
- `track_search(...)` → 4 of them

The parameter list is copy-pasted, in slightly different subsets, across five signatures. Adding one new option means touching every signature and every call site.

### Control flow (standard search pipeline)
1. **Validate** inputs.
2. **Cache check** — build a key, return early on a hit via the walrus operator `:=`.
3. **Build** the backend query dict.
4. **Execute** the search (stub returns 4 hardcoded videos).
5. **Track/log** the search.
6. **Post-process** through three chained filters (`filter_by_duration`, `exclude_shorts`, `limit_results`).

### Other symptoms
- `validate_search` only actually uses `query` and `max_results`, yet its signature demands all 8 — dead parameters.
- `get_cache_key` includes `language` but excludes `max_results` (cache keyed on what changes results, not how many).

### Tracing `main`
Call: `duration="long", region="NL", include_shorts=False, max_results=10`. Only videos > 1200s survive `filter_by_duration` when `duration == "long"`, so the 4 hardcoded videos reduce to one:

```
- Clean architecture in Python
```

---

## Code walk-through: `after.py` — Introduce Parameter Object

`after.py` fixes exactly the smell above. It's a textbook **Introduce Parameter Object** refactor.

### The core move: `VideoSearchQuery` dataclass
The 9 loose parameters — with their defaults — become fields on one `@dataclass(frozen=True)`. The defaults that lived on `search_videos`'s signature now live in one place. The object doesn't just carry data — it absorbs two responsibilities that used to be free functions.

### What moved onto the object
1. **Validation → `__post_init__`** — the standalone `validate_search` function is gone; its logic runs automatically right after construction. You **cannot construct an invalid `VideoSearchQuery`** — the object is always valid by the time it exists.
2. **Cache key → `@property`** — `get_cache_key` becomes `search.cache_key`, derived from the object that owns the data.

### `search_videos` collapses
Signature goes from 9 parameters to `def search_videos(search: VideoSearchQuery)`. Every hand-copied keyword-forwarding block disappears:

| `before.py` | `after.py` |
|---|---|
| `validate_search(query=..., ×8)` | *gone* — done at construction |
| `get_cache_key(query=..., ×8)` | `search.cache_key` |
| `build_search_query(query=..., ×9)` | `build_search_query(search)` |
| `track_search(query=..., ×4)` | `track_search(search)` |

### What deliberately did NOT change
The three tail filters stay as `(videos, scalar)` — they're genuinely reusable that way. Not everything should take the parameter object; passing `search.duration` rather than the whole object keeps them decoupled. Only the functions drowning in the shared parameter set were changed.

### Payoff
- **Adding a search option** = add one field to `VideoSearchQuery`. No signature edits, no call-site edits across five functions.
- **Invalid states are unrepresentable** — validation enforced at construction, not by discipline.
- **`main` reads as data, then action** — build a `VideoSearchQuery`, pass it to `search_videos`.

Both files produce the same output (`- Clean architecture in Python`). Subtle behavior difference: in `before.py` a helper could be called with a bad `max_results` because validation was a separate step; in `after.py` that's impossible — the value never reaches a helper unvalidated.

---

## Structural pattern matching: `match`/`case` (`pattern_matching.py`)

`pattern_matching.py` starts from the `after.py` code (same `VideoSearchQuery` parameter object) and layers on structural pattern matching (PEP 634, Python 3.10+). The payoff builds directly on the refactor: because everything is bundled into one object, you can match on its shape and destructure it in a single readable statement.

### Intuition
> `if` asks *"is this value equal to that?"* — `match` asks *"does this thing have this shape, and while checking, hand me the pieces I want."*

**Step 0 — a smarter `if`/`elif`** (cases run top-to-bottom, first match wins; `_` is the wildcard):
```python
match x:
    case 0: return "zero"
    case 1: return "one"
    case _: return "many"
```

**Step 1 — a bare name CAPTURES instead of comparing.** Trap: `case 0` compares (equal to 0?), but `case other` *assigns* x into `other`:
```python
match x:
    case 0:     print("zero")
    case other: print(f"got {other}")   # binds x into `other`
```

**Step 2 — match on an object's SHAPE.** Inside a `case`, `Point(...)` is NOT constructing — it's a question: "is it a `Point`, and do these fields match?"
```python
match p:
    case Point(x=0, y=0):       print("origin")
    case Point(x=0, y=yval):    print(f"y-axis at {yval}")   # x MUST be 0, capture y
    case Point(x=xval, y=yval): print(f"at {xval},{yval}")
```
- `field=literal` → **GUARD** (must be equal)
- `field=variable` → **CAPTURE** (bind it out)

Both jobs — *test* and *extract* — happen in one line.

### Real usage in the file
```python
# build_search_query — guard on sort_by, capture max_results
case VideoSearchQuery(sort_by="views", max_results=max_results):
    ...   # "is search a VideoSearchQuery with sort_by == 'views'? pull out max_results"

# track_search — two guards (region, include_shorts) + one capture (query)
case VideoSearchQuery(query=query, region="NL", include_shorts=False):
    ...   # all guards must hold together; query is bound out
```

### Why it beats plain `if`
| Plain `if` | `match`/`case` |
|---|---|
| `if isinstance(s, VideoSearchQuery) and s.region == "NL" and not s.include_shorts:` then read `s.query` | `case VideoSearchQuery(query=query, region="NL", include_shorts=False):` |
| type check + value conditions + extraction spread across lines | collapse into one declarative line that looks like the object it matches |

Pattern matching shines exactly when you have a structured object and want to branch on its *shape and field values* while pulling pieces out — declaratively, in one statement.
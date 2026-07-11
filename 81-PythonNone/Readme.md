# How to avoid None checks

1. Use better defaults
2. Do validation sooner -> raw data adheres to constraints and fail fast
3. Rely on exceptions -> when return type from method has an option for None ex. int | None
4. Be explicit about modeling states ex. ReadyDrone (strict state of DroneTelematory) - extend to OfflineDrone, ConnectedDrone and then pass particular state toe particular logic - try valid defined states and have less occurances of invalid states not defined
5. Use NULL object pattern -> Doing nothing is a valid operation, Ex. RouteDiagnostics -> have NullDiagnostics do nothing use in place of None
6. Sentinel object -> Null valid then another value for not provided. Define special object. Ex. MISSING = object() -> this represent missing value, in api - caller passing None vs no value passed
7. Result Object -> return result indicating something has been rejected or failed. type RouteResult = Route | RouteFailed, RouteFailed class -> defined seperately - used in functional programming or rust. Python -> returns package. In python, exceptions preferred instead of returns.

Defensive programming - useful at edges ex. Raw data from drone or API retrieval. Inside domain core, need to be really strict. ReadyDrone strict vs DroneTelematory - get raw data can be invalid, 
Separating raw and messy data at edge and clean / strict data use in core logic.

---

# before.py → after.py Walkthrough

A drone-delivery route assigner refactored to eliminate pervasive `None` handling.
`before.py` is the problem version; `after.py` applies the techniques listed above.

## before.py — the problems

- **`Route`** (mutable): `start` / `destination` default to `None`, so a `Route()` can exist
  half-built and invalid.
- **`DroneTelemetry`**: three of four fields are `X | None` — every consumer must null-check all of them.
- **`Delivery.avoid_zones`**: `list[GeoFence] | None = None` (author's own comment says an empty
  list default would be better).
- **`WeatherReport.wind_speed`**: `int | None`.
- **`assign_delivery`** returns `Route | None` and is a pyramid of `None` checks:
  - `if diagnostics is not None` repeated ~7 times.
  - Wind-safety check nested 4 levels deep.
  - Every failure is a bare `return None` — caller learns *nothing* about why.
  - Passes a maybe-`None` `telemetry.location` into a function expecting non-`None`;
    only safe because of an earlier guard the type system can't see.

## after.py — the fixes

`assign_delivery` shrinks from ~57 lines of nested checks to ~25 lines of straight-line logic.

| Before | After | Technique |
|---|---|---|
| `avoid_zones: list \| None = None` | `field(default_factory=list)` | Better defaults |
| Nullable `DroneTelemetry` used everywhere | `prepare_drone` → validated `ReadyDrone` | Fail fast + state modeling |
| `return None` on failure | `raise RouteRejected(reason)` | Exceptions / Result |
| `if diagnostics is not None` ×7 | `NullDiagnostics` default | Null Object |
| `Route()` half-built, mutable | frozen `Route`, built once | Make invalid states unrepresentable |
| 4-level nested wind check | flat `if ...: raise` | (consequence of all the above) |

### 1. Better defaults
`Delivery.avoid_zones` and `Route.avoid_zones` use `field(default_factory=list)` — no `| None`,
so the `if delivery.avoid_zones is not None` guard disappears.

### 2. Fail fast + validated type
Two types instead of one nullable type:
- **`DroneTelemetry`** — raw sensor input, still `X | None`.
- **`ReadyDrone`** — validated, non-nullable fields.

**`prepare_drone`** is the gate: checks each field once, raises `ValueError` if `None`, returns a
`ReadyDrone`. After the gate, `None` is impossible, so `assign_delivery` (which takes `ReadyDrone`)
never null-checks again. The invariant is enforced by the type system.

### 3. Exceptions instead of `None` returns
Return type is `Route` (not `Route | None`). New `RouteRejected` exception replaces every
`return None` and carries a *reason*. `main` uses `try/except/else` instead of `if route is None`.

### 4. Null Object pattern
Kills the `if diagnostics is not None` repetition:
- `RouteDiagnostics` — a `Protocol` (structural interface).
- `ConsoleDiagnostics` — prints.
- `NullDiagnostics` — does nothing; used as the default arg.

Call `diagnostics.record(...)` unconditionally.
⚠️ Caveat: `NullDiagnostics()` as a default arg is a mutable default evaluated once — harmless here
(stateless) but a general foot-gun.

### 5. Immutability (supporting change)
`Route` is now `frozen=True` with required non-nullable `start` / `destination`. It can only be
constructed complete and valid, all at once — no invalid intermediate state to guard.

## Net effect
`None` handling is pushed to **one boundary** (`prepare_drone`); the core business logic operates on
types guaranteed valid, so it reads as a simple linear sequence of rules.

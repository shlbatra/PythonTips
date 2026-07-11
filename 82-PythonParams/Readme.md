## Similar Params used across lot of methods and keep growing as code grows with new functionalities
1. Use keyword args but still methods require many arg variations so not solve underlying issue of params growing and also shared across different methods
# How to solve
1. Group data that pass around in a common object -> dataclass ex. VideoSearchQuery -> add all args, just pass VideoSearchQuery arg to all methods and simplify
2. Include validation at dataclass level next instead of method in __post_init method -> Once we have object - make sure its valid
3. Make cache_key as property instead of method ->  with get_cache_key method - search_videos much simpler
4. To add more fields, just do at dataclass in query object and use only where required in methods

# When not to use 
1. Would all functions need to all arguments. Ex.normalize_region - might not require anything other than region - Stamp Coupling - accidently use other things not reqd
2. Use mostly higher level workflow where all args are actually required

# Pattern matching
1. Structural pattern matching, in build_search_query or track_search instead of having if-else statemenent

---

## Summary: before.py -> after.py -> pattern_matching.py

**before.py — the smell.** `search_videos` takes 9 params and re-threads them by hand into 5 helpers (`validate_search`, `get_cache_key`, `build_search_query`, `track_search`). Params are copy-pasted in different subsets across every signature; adding one option means editing all of them. `validate_search` even takes 8 params but only uses 2 (dead params).

**after.py — Introduce Parameter Object.** The 9 params + defaults collapse into one `VideoSearchQuery(frozen=True)` dataclass, which also absorbs two jobs: validation moves into `__post_init__` (object can't exist invalid), and the cache key becomes a `@property`. Every helper now takes one `search` arg. Tail filters (`filter_by_duration`, etc.) deliberately stay `(videos, scalar)` — they don't need the whole object (avoids stamp coupling). Same output as before.

**pattern_matching.py — match/case on the object.**
- Intuition: `if` asks *"is this equal to that?"*; `match` asks *"does this have this shape, and hand me the pieces."*
- Cases run top-to-bottom, first wins; `_` = wildcard.
- Inside a case, `VideoSearchQuery(...)` is a question, not construction: `field=literal` is a **guard** (must equal), `field=variable` is a **capture** (bind it out) — test + extract in one line.
- Used in `build_search_query` (guard on `sort_by`, capture `max_results`) and `track_search` (guard on `region`+`include_shorts`, capture `query`), replacing nested `if`/`and` chains with one declarative line.

All three files produce the same result: `- Clean architecture in Python`.


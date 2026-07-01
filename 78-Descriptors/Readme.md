# Python Descriptors

## How the files build on each other

| File | Concept | How it connects |
|------|---------|-----------------|
| `minimal.py` | Basic `__get__`/`__set__` descriptor | Introduces the descriptor protocol — intercept attribute read/write |
| `non_data.py` | Non-data vs data descriptor lookup priority | Non-data (`__get__` only) can be shadowed by instance `__dict__`; data (`__get__` + `__set__`) always wins |
| `tiny_prop.py` | Decorator that returns a descriptor | Shows `@property` is just a decorator wrapping a function inside a descriptor |
| `validated.py` | Reusable validation via data descriptors | Combines `__get__`, `__set__`, `__set_name__`, cast + validators for declarative field validation |
| `lazy_prop.py` | Compute-once caching via non-data descriptor | Uses non-data descriptor shadowing as a feature — instance `__dict__` caches the result after first access |

import json
from functools import wraps
from typing import Any, Callable

# ------------------------------------------------------------
# Generic Types
# ------------------------------------------------------------

type PredicateFn[T] = Callable[[T], bool]
type RuleDef = Callable[..., bool]
type PredicateFactory[T] = Callable[..., Predicate[T]] # callable passing any number of args and return is a Predicate


# ------------------------------------------------------------
# Global Rule Registry
# ------------------------------------------------------------

RULES: dict[str, PredicateFactory[Any]] = {}


# ------------------------------------------------------------
# Predicate
# ------------------------------------------------------------


class Predicate[T]:
    """
    A composable predicate that supports &, |, and ~ operators.
    Wraps a function (T -> bool).
    """

    def __init__(self, fn: PredicateFn[T]):
        self.fn = fn

    def __call__(self, obj: T) -> bool:
        return self.fn(obj)

    def __and__(self, other: Predicate[T]) -> Predicate[T]:
        return Predicate(lambda x: self(x) and other(x))

    def __or__(self, other: Predicate[T]) -> Predicate[T]:
        return Predicate(lambda x: self(x) or other(x))

    def __invert__(self) -> Predicate[T]:
        return Predicate(lambda x: not self(x))


# ------------------------------------------------------------
# Decorators
# ------------------------------------------------------------

#  Used for simple predicates with no parameters. It wraps a function T -> bool into a Predicate object.
def predicate[T](fn: PredicateFn[T]) -> Predicate[T]:
    @wraps(fn)
    def wrapper(obj: T) -> bool:
        return fn(obj)

    return Predicate(wrapper)


# Used for parameterized predicates. It creates a factory that produces Predicate objects based on arguments.
def rule[T](fn: RuleDef) -> PredicateFactory[Any]:
    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Predicate[T]:
        return Predicate(lambda obj: fn(*args, obj, **kwargs))

    RULES[fn.__name__] = wrapper # registers the rule in RULES dict (line 67), enabling config-driven rule loading via load_rule_from_config().  
    return wrapper


# ------------------------------------------------------------
# Config Loader
# ------------------------------------------------------------

#  JSON Config → Look up rules in RULES registry → Create Predicates → Combine with AND/OR
def load_rule_from_config(path: str) -> Predicate[Any]:
    """
    Load a rule from a JSON config file that looks like:

    {
      "logic": "AND",
      "conditions": [
        {"name": "is_active", "args": []},
        {"name": "older_than", "args": [30]}
      ]
    }

    The returned object is a composed Predicate[Any].
    """

    with open(path) as f:
        config = json.load(f)

    preds: list[Predicate[Any]] = []
    
    # For each condition: look up rule by name, call factory with args
    for cond in config["conditions"]:
        name = cond["name"]
        args = cond.get("args", [])

        if name not in RULES:
            raise ValueError(f"Unknown rule: {name}")

        factory = RULES[name]
        predicate_obj = factory(*args)
        preds.append(predicate_obj)

    # Combine predicates using & (AND) or | (OR)  
    combined = preds[0]
    logic = config["logic"]

    for p in preds[1:]:
        combined = (combined & p) if logic == "AND" else (combined | p) # preds[0] & preds[1] & preds[2] ... 

    return combined
from typing import Any, Callable, Self


class lazy_property[T]:
    def __init__(self, func: Callable[[Any], T]) -> None:
        self.func = func
        self.name = func.__name__
        self.storage_name = f"_{self.name}"

    def __get__(self, instance: Any | None, owner: type) -> T | Self:
        """
          This is where non_data.py pays off. Because lazy_property has no __set__, the lookup order is:

            1. Data descriptors       ← not this (no __set__)
            2. Instance __dict__      ← wins after first computation
            3. Non-data descriptors   ← wins only on first access

            On first access, _revenue_by_country doesn't exist on the instance, so the descriptor's __get__ runs and computes it. 
            After setattr stores the result on the instance, the instance __dict__ shadows the descriptor on all future
            accesses. Python never even calls __get__ again — the cached value is found first at priority level 2.
        """
        if instance is None:
            return self
        if hasattr(instance, self.storage_name): # where cache checked for specific storage name already compute
            return getattr(instance, self.storage_name)
        value = self.func(instance)
        setattr(instance, self.storage_name, value) # if not computed before then computed on line above
        return value


class Report:
    def __init__(self, rows: list[dict[str, Any]]) -> None:
        self.rows = rows

    @lazy_property
    def revenue_by_country(self) -> dict[str, float]:
        print("computing revenue_by_country...")
        result: dict[str, float] = {}
        for r in self.rows:
            country = str(r["country"])
            revenue = float(r["revenue"])
            result[country] = result.get(country, 0.0) + revenue
        return result


def main() -> None:
    rows: list[dict[str, Any]] = [
        {"country": "NL", "revenue": 10},
        {"country": "NL", "revenue": 5},
    ]

    rep = Report(rows)
    print(rep.revenue_by_country)
    print(rep.revenue_by_country)  # cached


if __name__ == "__main__":
    main()
# Avoid nested loop structures in Python code

1. Is the right data structure used ?
2. Behavior in the right place - level of what you are doing Ex. calculate order total -> low level calculation not in report generation but at order level. If data only from low level, then part of object
and not at higher level.
3. Too many responsibilities in report method - find orders, filter paid ones, calculate total, apply discount and build output - too much, Think about reasons to change ex. order structure or disc logic change or summary change - many reasons to change - they should be 1 main reason to change.
4. Not fix nested loops -> still as part of seperate methods - but methods simple and no mix responsibility. 
5. Wrong abstraction level -> Work with primitive ex. Int float instead of Order, OrderItem, Customer - get messy code - list of lists
6. Fear of introducing extra data structures -> not avoid dict or tuples
7. Incremental growth - add condition or loop - so keep track. 

## Summary of changes (before.py -> after.py)

| Concern | before.py | after.py |
|---|---|---|
| Nesting | 3 nested loops (customer -> order -> item) | 1 loop + comprehensions |
| Join cost | O(customers x orders) - rescan all orders per customer | O(orders) group once, O(1) lookup per customer |
| Item total | inline in report generation | `Order.total` property |
| Discount rule | inline `if` in the report loop | `apply_discount()` pure function |
| Filtering paid orders | inline `if order.status == "paid"` | `paid_orders()` helper |
| Testability | one big function | small single-responsibility functions |

Key moves:
1. **Push per-object math onto the object** - the per-item total became an `Order.total` property instead of living in the report loop.
2. **Group instead of join** - `group_orders_by_customer` builds a `dict[customer_id, list[Order]]` in one pass, replacing the nested "for each customer, scan all orders" join.
3. **Split responsibilities** - `paid_orders`, `apply_discount`, and `build_customer_summary` each do one job, so each has one reason to change.
4. **Flatten the orchestrator** - `generate_customer_report` is now a single flat loop: look up the customer's orders, skip if none, build the summary.

Behavior is unchanged - both print `Alice: 1 orders, total spent = 99.0` and `Bob: 1 orders, total spent = 40`.
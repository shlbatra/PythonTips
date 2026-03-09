
# Problem
Mixing domain logic with API and framework code ex. sqlalchemy
Issue with testing as need to know database connection for unit tests
Domain language coupled with api - if change framework ex. NOSQL or move away from FastAPI then rewrite everything
So, decouple things correctly

# Ports and Adapters

Code across 3 layers -
1. Domain - Rules, decisions - not import from other frameworks
2. Ports - Interfaces the domain needs ex. ABC, Protocols - InventoryPort , PaymentPort, EmailPort
3. Adapters - Specific framework implementations ex. SQLAlchemy adapter implements Inventory Port, FastAPI translates http to domain errors


Commands to run code 

uvicorn main:app --reload

curl -s -X POST "http://127.0.0.1:8000/orders" \
-H "Content-Type: application/json" \
-d '{"user_id":1, "sku":"ABC","qty":3}' | python -m json.tool

1. Decouple domain with frameworks
Give language and type and errors

2. Domain only includes Business logic and ports include interface

3. Framework is passed via API itself irrespective of domain logic so unit tests can be mocked

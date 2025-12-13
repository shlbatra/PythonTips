"""
curl -X POST http://localhost:8000/process/ \
    -H "Content-Type: application/json" \
    -d '[
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 11},
                {"name": "Sahil", "age": 37}
          ]'

curl -X POST http://localhost:8000/process/ \
    -H "Content-Type: application/json" \
    -d '[
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": null}, 
                {"name": "Sahil", "age": 37}
          ]'

curl -X POST http://localhost:8000/process/ \
      -H "Content-Type: application/json" \
      -d '[{"name": "Alice", "age": 30}, {"name": null, "age": 25}]'
"""

from fastapi import FastAPI, Depends, Body
from typing import Protocol, Any
import uvicorn

type Data = list[dict[str, Any]]

app = FastAPI()


# === Transformer interface and implementation ===
class Transformer(Protocol):
    def transform(self, data: Data) -> Data: ...


class CleanMissingFields:
    def transform(self, data: Data) -> Data:
        return [row for row in data if row["age"] is not None]


class CleanMissingFieldsName:
    def transform(self, data: Data) -> Data:
        return [row for row in data if row["name"] is not None]


# === Dependency ===
def get_transformer() -> Transformer:
    return CleanMissingFields()


# === Endpoint ===
@app.post("/process/")
def process_data(
    data: Data = Body(...),  # <-- Tell FastAPI this comes from the request body
    transformer: Transformer = Depends(get_transformer)
):
    cleaned = transformer.transform(data)
    return {"cleaned": cleaned}


def main():
    uvicorn.run("fastapi_app:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
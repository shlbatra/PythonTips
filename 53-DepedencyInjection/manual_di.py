import json
from typing import Protocol, Any

type Data = list[dict[str, Any]] # Ex. [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]


# Interfaces

class DataLoader(Protocol):
    def load(self) -> Data:
        ...

class Transformer(Protocol):
    def transform(self, data: Data) -> Data:
        ...

class Exporter(Protocol):
    def export(self, data: Data) -> None:
        ...

# Concrete Implementations

class InMemoryDataLoader:
    def load(self) -> Data:
        return [{"name": "Alice", "age": 30}, {"name": "Bob", "age": None}, {"name": "Charlie", "age": 25}]
    
class CleanMissingFields:
    def transform(self, data: Data) -> Data:
        return [row for row in data if row.get("age") is not None]
    
class JsonExporter:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        
    def export(self, data: Data) -> None:
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

# === Pipeline ===

class DataPipeline:

    def __init__(self, loader: DataLoader, transformer: Transformer, exporter: Exporter) -> None:
        self.loader = loader
        self.transformer = transformer
        self.exporter = exporter

    def run(self) -> None:
        # Hardcoded loader
        data = self.loader.load()

        # Hardcoded transformation
        cleaned = self.transformer.transform(data)

        #Hardcoded export
        self.exporter.export(cleaned)

# === Main function: inject dependencies manually ===

def main() -> None:
    loader = InMemoryDataLoader()
    transformer = CleanMissingFields()
    exporter = JsonExporter("output.json")

    pipeline = DataPipeline(loader, transformer, exporter)
    pipeline.run()
    print("Data pipeline executed successfully.")

if __name__ == "__main__":
    main()
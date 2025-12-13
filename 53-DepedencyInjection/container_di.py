import json
from typing import Protocol, Any, Callable

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


# === Simple DI container ===
class Container:
    def __init__(self) -> None:
        self._providers: dict[str, tuple[Callable[[], Any], bool]] = {} # Ex. {"DataLoader": (InMemoryDataLoader, False)}
        self._singletons: dict[str, Any] = {} # Ex. {"DataLoader": InMemoryDataLoader}

    def register(self, name: str, provider: Callable[[], Any], singleton: bool = False) -> None: # Ex, register("DataLoader", InMemoryDataLoader, True), With args. Ex. register("JsonExporter", lambda: JsonExporter("output.json"))
        self._providers[name] = (provider, singleton)

    def resolve(self, name: str) -> Any:
        if name in self._singletons:
            return self._singletons[name]
        
        if name not in self._providers:
            raise ValueError(f"No provider registered for {name}")
        
        provider, singleton = self._providers[name]
        instance = provider()

        if singleton:
            self._singletons[name] = instance

        return instance
        


# === Main function: runner ===
# The lambda acts as a "deferred call" — it packages up the function and its arguments into a callable that can be invoked later with no arguments.


def main() -> None:

    container = Container()
    container.register("DataLoader", InMemoryDataLoader, singleton=True)
    container.register("Transformer", CleanMissingFields)
    container.register("Exporter", lambda: JsonExporter("output.json"))

    container.register(
        "DataPipeline",
        lambda: DataPipeline(
            loader=container.resolve("DataLoader"),
            transformer=container.resolve("Transformer"),
            exporter=container.resolve("Exporter"),
        )
    )

    pipeline: DataPipeline = container.resolve("DataPipeline")
    pipeline.run()
    print("Data pipeline executed successfully.")

if __name__ == "__main__":
    main()
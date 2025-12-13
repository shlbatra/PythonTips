import json
from typing import Any

type Data = list[dict[str, Any]] # Ex. [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]

class DataPipeline:
    def run(self) -> None:
        # Hardcoded loader
        data = self._load_data_from_csv()

        # Hardcoded transformation
        cleaned = [row for row in data if row.get("age") is not None]

        #Hardcoded export
        self._export_to_json(cleaned)

    def _load_data_from_csv(self) -> Data:
        # Simulate loading data from a CSV file
        return [{"name": "Alice", "age": 30}, {"name": "Bob", "age": None}, {"name": "Charlie", "age": 25}]
    
    def _export_to_json(self, data: Data) -> None:
        with open("output.json", "w") as f:
            json.dump(data, f, indent=2)

def main() -> None:
    pipeline = DataPipeline()
    pipeline.run()
    print("Data pipeline executed successfully.")

if __name__ == "__main__":
    main()
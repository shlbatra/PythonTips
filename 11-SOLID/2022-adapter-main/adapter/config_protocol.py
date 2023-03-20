from typing import Any, Protocol


#get config value
class Config(Protocol):
    def get(self, key: str, default: Any = None) -> Any:
        """Return the value associated with key"""

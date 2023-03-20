#undo and redo part not transaction - take care in bankcontroller with history and pointer

from typing import Protocol


class Transaction(Protocol):
    def execute(self) -> None:
        ...

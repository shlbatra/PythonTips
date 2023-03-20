from dataclasses import dataclass

#dont need balance - state as txn history 
@dataclass
class Account:
    name: str
    number: str
    _balance_cache: int = 0 #cache value not concerned about 

    def deposit(self, amount: int) -> None:
        self._balance_cache += amount

    def withdraw(self, amount: int) -> None:
        if amount > self._balance_cache:
            raise ValueError("Insufficient funds")
        self._balance_cache -= amount

    def clear_cache(self) -> None:
        self._balance_cache = 0

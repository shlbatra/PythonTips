# Domain needs interface to manage depedencies 

from typing import Protocol


class InventoryPort(Protocol):
    def exists_sku(self, sku: str) -> bool: ... # check if sku exists
    def get_stock(self, sku: str) -> int: ... # check stock for sku
    def reserve(self, sku: str, qty: int) -> int: ... # remaining stock after reserving qty of sku

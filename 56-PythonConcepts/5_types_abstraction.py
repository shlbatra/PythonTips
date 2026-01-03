from typing import Protocol, Callable

class Logger(Protocol):
    def info(self, message: str) -> None: 
        ...

    def error(self, message: str) -> None: 
        ...


def process_order(order_id: int, logger: Logger) -> None: # Using a Protocol for type abstraction
    logger.info(f"Processing order {order_id}")


ImageExporter = Callable[[bytes], None] # Function with bytes argument and None return type

def export_image(data: bytes, exporter: ImageExporter) -> None:
    exporter(data)
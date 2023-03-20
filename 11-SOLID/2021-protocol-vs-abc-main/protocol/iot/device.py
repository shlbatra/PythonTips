from typing import Protocol

from iot.message import MessageType


class Device(Protocol):
    def connect(self) -> None:
        ...

    def disconnect(self) -> None:
        ...

    def send_message(self, message_type: MessageType, data: str) -> None:
        ...

    def status_update(self) -> str:
        ...

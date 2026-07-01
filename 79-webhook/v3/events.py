from datetime import UTC, datetime
from enum import StrEnum
from typing import Any, Callable
from uuid import UUID, uuid4

from pydantic import BaseModel


class EventType(StrEnum):
    LINK_CREATED = "link.created"
    LINK_CLICKED = "link.clicked"


class Event(BaseModel):
    id: UUID
    type: EventType
    occurred_at: datetime
    data: dict[str, Any]


EventListener = Callable[[Event], None]


class EventBus:
    def __init__(self) -> None:
        self._listeners: dict[EventType, list[EventListener]] = {} # Link event types to list of event listners

    def subscribe(
        self,
        event_type: EventType,
        listener: EventListener,
    ) -> None:
        self._listeners.setdefault(event_type, []).append(listener)

    def publish(
        self,
        event_type: EventType,
        data: dict[str, Any],
    ) -> Event:
        event = Event(
            id=uuid4(),
            type=event_type,
            occurred_at=datetime.now(UTC),
            data=data,
        ) # also store in database and track event later on

        for listener in self._listeners.get(event.type, []):
            listener(event)

        return event

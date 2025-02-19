from abc import ABC, abstractmethod

from src.models.entities.eventos_link import EventosLink


class EventosLinkRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, event_id: str, subscriber_id: int) -> None:
        pass

    @abstractmethod
    def select_event(self, event_id: str, subscriber_id: int) -> EventosLink:
        pass

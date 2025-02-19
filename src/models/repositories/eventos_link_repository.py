import random

from src.models.configs.connection import DBConnectionHandler
from src.models.entities.eventos_link import EventosLink
from src.models.repositories.interfaces.eventos_link_repository import (
    EventosLinkRepositoryInterface,
)


class EventosLinkRepository(EventosLinkRepositoryInterface):
    def insert(self, event_id: str, subscriber_id: int) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                formatted_link = f"evento-{event_id}-inscrito-{subscriber_id}-{''.join(random.choices('0123456789', k=7))}"
                new_events_link = EventosLink(
                    evento_id=event_id, inscrito_id=subscriber_id, link=formatted_link
                )
                db_connection.session.add(new_events_link)
                db_connection.session.commit()
                return formatted_link
            except Exception as e:
                db_connection.session.rollback()
                raise e

    def select_event(self, event_id: str, subscriber_id: int) -> EventosLink:
        with DBConnectionHandler() as db_connection:
            return (
                db_connection.session.query(EventosLink)
                .filter(
                    EventosLink.evento_id == event_id,
                    EventosLink.inscrito_id == subscriber_id,
                )
                .one_or_none()
            )

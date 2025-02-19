from src.models.repositories.eventos_link_repository import EventosLinkRepository
import pytest


@pytest.mark.skip("insert events link into db")
def test_insert_events_link():
    event_id = 12
    subscriber_id = 123
    event_link_repository = EventosLinkRepository()

    event_link_repository.insert(event_id, subscriber_id)

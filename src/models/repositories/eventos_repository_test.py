from .eventos_repository import EventosRepository
import pytest

@pytest.mark.skip("Insert in DB")
def test_insert_events():
    # Arrange
    event_name = "Test Event"
    repository = EventosRepository()
    # Act
    repository.insert(event_name)
    # Assert
    assert repository.select_event(event_name) is not None

def test_select_event():
    # Arrange
    event_name = "Test Event 2"
    repository = EventosRepository()
    # Act
    repository.insert(event_name)
    # Assert
    # assert repository.select_event(event_name) is not None
    event = repository.select_event(event_name)
    print(event)
    print(event.nome)

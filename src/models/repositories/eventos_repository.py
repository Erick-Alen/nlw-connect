from src.models.configs.connection import DBConnectionHandler
from src.models.entities.eventos import Eventos


class EventosRepository:
    def insert(self, event_name: str) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_event = Eventos(nome=event_name)
                db_connection.session.add(new_event)
                db_connection.session.commit()
            except Exception as e:
                db_connection.session.rollback()
                raise e

    def select_event(self, event_name: str) -> Eventos:
        with DBConnectionHandler() as db_connection:
            return (
                db_connection.session.query(Eventos)
                .filter(Eventos.nome == event_name)
                .one_or_none()
            )

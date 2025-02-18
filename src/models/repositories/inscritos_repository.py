from typing import Dict

from src.models.configs.connection import DBConnectionHandler
from src.models.entities.inscritos import Inscritos


class InscritosRepository:
    def insert(self, subscriber_infos: Dict[str, str]) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_subscriber = Inscritos(
                    nome=subscriber_infos.get("nome"),
                    email=subscriber_infos.get("email"),
                    evento_id=subscriber_infos.get("evento_id"),
                )
                db_connection.session.add(new_subscriber)
                db_connection.session.commit()
            except Exception as e:
                db_connection.session.rollback()
                raise e

    def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
        with DBConnectionHandler() as db_connection:
            return (
                db_connection.session.query(Inscritos)
                .filter(Inscritos.email == email, Inscritos.evento_id == evento_id)
                .one_or_none()
            )

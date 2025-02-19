from typing import Dict, List, Tuple

from sqlalchemy import desc, func

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

    def select_subscriber_by_link(self, link: str, event_id: int) -> Inscritos:
        with DBConnectionHandler() as db_connection:
            return (
                db_connection.session.query(Inscritos)
                .filter(Inscritos.link == link, Inscritos.evento_id == event_id)
                .all()
            )

    def select_referral_ranking(self, event_id: int) -> List[Tuple]:
        with DBConnectionHandler() as db_connection:
            return (
                db_connection.session.query(
                    Inscritos.link,
                    func.count(Inscritos.id).label("Total users subscribed by link"),
                )
                .filter(
                    Inscritos.evento_id == event_id, Inscritos.evento_id.isnot(None)
                )
                .group_by(Inscritos.link)
                .order_by(desc("Total users subscribed by link"))
                .all()
            )

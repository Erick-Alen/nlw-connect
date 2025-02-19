from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from src.models.entities.inscritos import Inscritos


class InscritosRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, subscriber_infos: Dict[str, str]) -> None:
        pass

    @abstractmethod
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
        pass

    @abstractmethod
    def select_subscriber_by_link(self, link: str, event_id: int) -> Inscritos:
        pass

    @abstractmethod
    def select_referral_ranking(self, event_id: int) -> List[Tuple]:
        pass

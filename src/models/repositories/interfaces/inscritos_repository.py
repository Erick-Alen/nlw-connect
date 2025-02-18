from abc import ABC, abstractmethod
from typing import Dict

from src.models.entities.inscritos import Inscritos


class InscritosRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, subscriber_infos: Dict[str, str]) -> None:
        pass

    @abstractmethod
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
        pass

from typing import Dict

from src.http_types import HttpRequest, HttpResponse
from src.models.repositories.interfaces.inscritos_repository import (
    InscritosRepositoryInterface,
)


class SubscribersCreator:
    def __init__(self, subs_repository: InscritosRepositoryInterface):
        self.__subs_repository = subs_repository

    def __check_sub(self, sub_email: str, event_id: int) -> None:
        response = self.__subs_repository.select_subscriber(
            email=sub_email, evento_id=event_id
        )
        if response:
            raise Exception("Subscriber already existe in this event")
        # raise Exception("Event already exists") if    response else None

    def __insert_sub(self, sub_info: Dict) -> None:
        self.__subs_repository.insert(sub_info)

    def __format_response(self, sub_info: Dict) -> HttpResponse:
        return HttpResponse(
            status_code=201,
            body={
                "data": {
                    "type": "Subscriber",
                    "count": 1,
                    "attributes": sub_info,
                }
            },
        )

    def create(self, http_request: HttpRequest) -> HttpResponse:
        sub_info = http_request.body["data"]
        sub_email = sub_info["email"]
        event_id = sub_info["evento_id"]
        self.__check_sub(sub_email, event_id)
        self.__insert_sub(sub_info)
        return self.__format_response(sub_info)

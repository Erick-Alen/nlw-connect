from src.http_types import HttpRequest, HttpResponse
from src.models.repositories.interfaces import EventosRepositoryInterface


class EventsCreator:
    def __init__(self, event_repository: EventosRepositoryInterface):
        self.__event_repository = event_repository

    def __check_event(self, event_name: str) -> None:
        response = self.__event_repository.select_event(event_name)
        if response:
            raise Exception("Event already exists")
        # raise Exception("Event already exists") if    response else None

    def __insert_event(self, event_name: str) -> None:
        self.__event_repository.insert(event_name)

    def __format_response(self, event_name: str) -> HttpResponse:
        return HttpResponse(
            status_code=201,
            body={
                "data": {
                    "type": "Event",
                    "count": 1,
                    "attributes": {"nome": event_name},
                }
            },
        )

    def create(self, http_request: HttpRequest) -> HttpResponse:
        event_info = http_request.body["data"]
        event_name = event_info["nome"]
        print({event_name})
        self.__check_event(event_name)
        self.__insert_event(event_name)
        return self.__format_response(event_name)

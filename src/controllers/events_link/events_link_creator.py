from src.http_types import HttpRequest, HttpResponse
from src.models.repositories.interfaces import EventosLinkRepositoryInterface


class EventsLinkCreator:
    def __init__(self, event_link_repository: EventosLinkRepositoryInterface):
        self.__event_link_repository = event_link_repository

    def __check_event_link(self, event_id: int, subscriber_id: int) -> None:
        response = self.__event_link_repository.select_event(event_id, subscriber_id)
        if response:
            raise Exception("Link already exists")
        # raise Exception("Event already exists") if    response else None

    def __insert_event_link(self, event_id: int, subscriber_id: int) -> str:
        return self.__event_repository.insert(event_id, subscriber_id)

    def __format_response(
        self, new_link: str, event_id: int, subscriber_id: int
    ) -> HttpResponse:
        return HttpResponse(
            status_code=201,
            body={
                "data": {
                    "type": "Event",
                    "count": 1,
                    "attributes": {
                        "link": new_link,
                        "event_id": event_id,
                        "subscriber_id": subscriber_id,
                    },
                }
            },
        )

    def create(self, http_request: HttpRequest) -> HttpResponse:
        event_link_info = http_request.body["data"]
        event_id = event_link_info["event_id"]
        subscriber_id = event_link_info["subscriber_id"]
        self.__check_event_link(event_id, subscriber_id)
        new_link = self.__insert_event_link(event_id, subscriber_id)
        return self.__format_response(self, new_link)

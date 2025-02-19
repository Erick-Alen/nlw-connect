from typing import List

from src.http_types import HttpRequest, HttpResponse
from src.models.repositories.interfaces import InscritosRepositoryInterface


class SubscribersManager:
    def __init__(self, subscribers_repo: InscritosRepositoryInterface):
        self.__subscribers_repo = subscribers_repo

    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
        link = http_request.param["link"]
        event_id = http_request.param["event_id"]
        subs = self.__subscribers_repo.select_subscriber_by_link(link, event_id)
        return self.__format_subs_by_link(subs)

    def __format_subs_by_link(self, subs: List):
        formatted_subs: List = []
        for sub in subs:
            formatted_subs.append(
                {
                    "id": sub.id,
                    "name": sub.name,
                    "email": sub.email,
                    "link": sub.link,
                    "event_id": sub.event_id,
                }
            )
        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "type": "Subscribers",
                    "count": len(formatted_subs),
                    "attributes": formatted_subs,
                }
            },
        )

    def get_referral_ranking(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event_ranking = self.__subscribers_repo.select_referral_ranking(
            event_id=event_id
        )
        return self.__format_event_ranking(event_ranking)

    def __format_event_ranking(self, event_ranking: List):
        formatted_event_ranking: List = []
        for position in event_ranking:
            formatted_event_ranking.append(
                {
                    "link": position.link,
                    "total_subscribers": position.event_id,
                }
            )
        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "Type": "Ranking",
                    "count": len(formatted_event_ranking),
                    "attributes": formatted_event_ranking,
                }
            },
        )

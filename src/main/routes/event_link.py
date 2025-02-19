from flask import Blueprint, jsonify, request

from src.controllers import EventsLinkCreator
from src.http_types.http_request import HttpRequest
from src.models.repositories import EventosLinkRepository
event_link_route_bp = Blueprint("event link", __name__)


@event_link_route_bp.route("/events_link", methods=["POST"])
def create_event():
    http_request = HttpRequest(body=request.json)
    eventos_repository = EventosLinkRepository()
    events_link_creator = EventsLinkCreator(eventos_repository)
    http_response = events_link_creator.create(http_request)
    # http_response = HttpResponse(body={"message": "Event created"}, status_code=201)
    return jsonify(http_response.body), http_response.status_code

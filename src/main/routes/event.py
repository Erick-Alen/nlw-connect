from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest
from src.validators.events_creator_validator import events_creator_validator
from src.controllers.events.events_creator import EventsCreator
from src.models.repositories.eventos_repository import EventosRepository

event_route_bp = Blueprint("event route", __name__)


@event_route_bp.route("/event", methods=["POST"])
def create_event():
    events_creator_validator(request)
    http_request = HttpRequest(body=request.json)
    eventos_repository = EventosRepository()
    events_creator = EventsCreator(eventos_repository)
    http_response = events_creator.create(http_request)
    # http_response = HttpResponse(body={"message": "Event created"}, status_code=201)
    return jsonify(http_response.body), http_response.status_code

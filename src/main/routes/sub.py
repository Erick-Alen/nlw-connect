from flask import Blueprint, jsonify, request

from src.controllers import SubscribersCreator
from src.http_types.http_request import HttpRequest
from src.models.repositories.inscritos_repository import InscritosRepository
from src.validators import subscribers_creator_validator

sub_route_bp = Blueprint("subscriber route", __name__)


@sub_route_bp.route("/subscribe", methods=["POST"])
def create_sub():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)
    inscritos_repository = InscritosRepository()
    subs_creator = SubscribersCreator(inscritos_repository)
    http_response = subs_creator.create(http_request)
    # http_response = HttpResponse(body={"message": "Event created"}, status_code=201)
    return jsonify(http_response.body), http_response.status_code

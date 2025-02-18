from flask import Blueprint, jsonify

event_route_bp = Blueprint("event route", __name__)

@event_route_bp.route('/event', methods=['POST'])
def create_event():
    return jsonify({'message': 'Event created'}), 201

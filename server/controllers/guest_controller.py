from flask import Blueprint, jsonify
from server.models.guest import Guest  

guest_bp = Blueprint("guests", __name__, url_prefix="/guests")

@guest_bp.route("/", methods=["GET"])
def get_guests():
    print(" Route hit: /guests")
    guests = Guest.query.all()
    print(" Guests:", guests)
    return jsonify([guest.to_dict() for guest in guests]), 200
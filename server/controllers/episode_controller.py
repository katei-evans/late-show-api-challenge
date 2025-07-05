from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models import db

episode_bp = Blueprint("episodes", __name__, url_prefix="/episodes")

@episode_bp.route("/", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([ep.to_dict() for ep in episodes]), 200

@episode_bp.route("/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify(episode.to_dict(rules=("appearances",))), 200

@episode_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return {"message": "Episode deleted successfully"}, 200
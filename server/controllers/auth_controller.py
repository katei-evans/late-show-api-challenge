from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from server.models.user import User
from server.models import db

auth_bp = Blueprint("auth", __name__, url_prefix="/")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "Username and password are required"}, 400

    if User.query.filter_by(username=username).first():
        return {"error": "Username already exists"}, 409

    new_user = User(username=username)
    new_user.password_hash = password

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.authenticate(password):
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token}), 200

    return {"error": "Invalid username or password"}, 401
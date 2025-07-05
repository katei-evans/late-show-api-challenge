from sqlalchemy_serializer import SerializerMixin
from server.models import db

class Guest(db.Model, SerializerMixin):
    __tablename__ = "guests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String)

    serialize_rules = ("-appearances.guest",)
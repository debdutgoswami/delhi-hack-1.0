import datetime, uuid
from api import bcrypt, app
from api.models import db

# Database ORMs
class Blood(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(15), unique=True)
    lat = db.Column(db.String(6))
    lon = db.Column(db.String(6))
    bloodgroup = db.Column(db.String(3))
    gender = db.Column(db.String(1))
    age = db.Column(db.String(3))
    created = db.Column(db.String(20))

    def __init__(
        self,
        first_name,
        last_name,
        phone,
        location,
        bloodgroup,
        gender,
        age,
        created,
    ):
        self.public_id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.lat = location[0]
        self.lon = location[1]
        self.bloodgroup = bloodgroup
        self.gender = gender
        self.age = age
        self.created = created

    def __repr__(self):
        return f"<Blood(name={self.first_name}, blood={self.bloodgroup})>"

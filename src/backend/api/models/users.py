import uuid
from api import bcrypt, app
from api.models import db

# Database ORMs
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    lat = db.Column(db.String(6))
    lon = db.Column(db.String(6))
    bloodgroup = db.Column(db.String(3))
    dob = db.Column(db.String(11))
    weight = db.Column(db.String(3))

    def __init__(
        self,
        first_name,
        last_name,
        email,
        password,
        location,
        bloodgroup,
        dob,
        weight,
    ):
        self.public_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode()
        self.lat = location[0]
        self.lon = location[1]
        self.bloodgroup = bloodgroup
        self.dob = dob
        self.weight = weight

    def __repr__(self):
        return f"<User(name={self.first_name})>"

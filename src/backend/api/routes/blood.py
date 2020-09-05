from flask import request, make_response, jsonify, url_for
import uuid, jwt, datetime
from functools import wraps

from api import app
from api.routes import api
from api.models import db
from api.models.users import User
from api.utils.blood import withinRange


@api.route("/find", methods=["POST"])
def find_blod():
    """
    Find blood
    """

    usersList = list()
    data = request.get_json(silent=True)

    bloodgroup, lat, lon, radius = (
        data.get("blood"),
        data.get("lat"),
        data.get("lon"),
        int(data.get("radius", 30)),
    )

    users = User.query.filter_by(bloodgroup=bloodgroup).all()

    for user in users:
        requestLocation = (lat, lon)
        donorLocation = (user.lat, user.lon)

        if withinRange(requestLocation, donorLocation, radius):
            usersList.append(user.serialize)

    return make_response(
        jsonify(
            {
                "message": "success",
                "users": usersList,
            }
        ),
        200,
    )


from flask import jsonify, Blueprint, request
from werkzeug.security import generate_password_hash

apiAdmins = Blueprint("apiAdmins", __name__, url_prefix="/api/admins")
@apiAdmins.route("/")
def admins():
    return 


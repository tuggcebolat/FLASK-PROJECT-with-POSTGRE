from flask import Flask,jsonify,Blueprint
apiUsers=Blueprint("apiUser",__name__,url_prefix="/api/users")

@apiUsers.route("/")
def index():
    return jsonify({"success":True,"message":"Hello Users"})

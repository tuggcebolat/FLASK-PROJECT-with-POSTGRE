from flask import Flask, jsonify
from api.users import apiUsers
from api.products import apiProducts
from api.admin import apiAdmins
from api.categories import apiCategories
from flask_cors import CORS

from ecommerce import createApp
from ecommerce.initialize_db import createDB


# APP AND DB CREATION ---------------------------------------------------------
app = createApp()
CORS(app)
createDB()
# ----------------

app.register_blueprint(apiUsers)
app.register_blueprint(apiProducts)
app.register_blueprint(apiAdmins)
app.register_blueprint(apiCategories)

@app.route("/")
def hello_world():
    return  "<p>Hello, World</p>"
@app.route("/profile")
def profile():
    return {"id":1,"name":"Tuğçe","age":"28","following":80,"followers":20}
if __name__=="__main__":
    app.run(debug=True)
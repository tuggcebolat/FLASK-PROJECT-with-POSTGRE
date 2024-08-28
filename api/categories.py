
from flask import Flask, jsonify, Blueprint, request

apiCategories = Blueprint("apiCategories", __name__,
                          url_prefix="/api/categories")


@apiCategories.route("/")
def categories():
    return 
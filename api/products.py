from flask import Flask, jsonify, Blueprint, request

apiProducts = Blueprint("apiProducts", __name__, url_prefix="/api/products")

@apiProducts.route("/")
def products():
   return jsonify({"success": True, "data": products, "count": len(products)})
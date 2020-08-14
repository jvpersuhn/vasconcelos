from flask import Blueprint, jsonify

from Ex13.app.history.action import get_all

app_empresa = Blueprint("app_address", __name__)

@app_empresa.route("/empresa", methods=["GET"])
def get():
    return jsonify([category.serialize() for category in get_all()]), 200
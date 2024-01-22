from flask import Blueprint, request, jsonify

from src.main.adapters.request import request_adapter

from src.main.composers.user_finder import user_finder_composer
from src.main.composers.user_insert import user_insert_composer

from src.validators.user_insert import user_insert_validator
from src.validators.user_finder import user_finder_validator

from src.errors.handler import handle_errors


route = Blueprint("user_routes", __name__)


@route.route("/user/find", methods=["GET"])
def find_user():
    http_response = None

    try:
        user_finder_validator(request)
        http_response = request_adapter(request, user_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@route.route("/user", methods=["POST"])
def register_user():
    http_response = None

    try:
        user_insert_validator(request)
        http_response = request_adapter(request, user_insert_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.services.user_service import UserService, UserError
from app.schemas.user_schema import user_schema, users_schema

user_bp = Blueprint("user", __name__)

# @user_bp.route("/", methods=["POST"])
# def create_user():
#     try:
#         data = request.json
#         user = UserService.create_user(
#             name=data["name"], email=data["email"], role=data.get("role", "USER")
#         )
#         return user_schema.jsonify(user), 201
#     except UserError as e:
#         return jsonify({"error": str(e)}), 400

@user_bp.route("/", methods=["POST"])
def create_user():
    try:
        data = request.json
        user = UserService.create_user(
            name=data["name"],
            email=data["email"],
            password=data["password"],  # get password from request
            role=data.get("role", "USER")
        )
        result = user_schema.dump(user)
        return jsonify(result), 201
    except UserError as e:
        return jsonify({"error": str(e)}), 400



# @user_bp.route("/", methods=["GET"])
# def get_users():
#     users = UserService.get_all_users()
#     return users_schema.jsonify(users), 200

# app/routes/user_routes.py

@user_bp.route("/", methods=["GET"])
def get_users():
    users = UserService.get_all_users()
    result = users_schema.dump(users)  # serialize list of users
    return jsonify(result), 200


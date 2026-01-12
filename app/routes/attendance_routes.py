from flask import Blueprint, request, jsonify
from app.services.attendance_service import AttendanceService, AttendanceError
from app.schemas.attendance_schema import (
    CheckInSchema,
    CheckOutSchema,
    AttendanceSessionSchema
)

attendance_bp = Blueprint("attendance", __name__)

check_in_schema = CheckInSchema()
check_out_schema = CheckOutSchema()
attendance_session_schema = AttendanceSessionSchema()
attendance_sessions_schema = AttendanceSessionSchema(many=True)


@attendance_bp.route("/check-in", methods=["POST"])
def check_in():
    try:
        data = check_in_schema.load(request.json)
        session = AttendanceService.check_in(
            user_id=data["user_id"],
            source=data.get("source", "WEB")
        )
        return jsonify(attendance_session_schema.dump(session)), 201
    except AttendanceError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(e)
        return jsonify({"error": "Internal server error"}), 500


@attendance_bp.route("/check-out", methods=["POST"])
def check_out():
    try:
        data = check_out_schema.load(request.json)
        session = AttendanceService.check_out(user_id=data["user_id"])
        return jsonify(attendance_session_schema.dump(session)), 200
    except AttendanceError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(e)
        return jsonify({"error": "Internal server error"}), 500


@attendance_bp.route("/history/<int:user_id>", methods=["GET"])
def history(user_id):
    try:
        sessions = AttendanceService.get_user_history(user_id)
        return jsonify(attendance_sessions_schema.dump(sessions)), 200
    except AttendanceError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(e)
        return jsonify({"error": "Internal server error"}), 500


@attendance_bp.route("/active", methods=["GET"])
def active_users():
    try:
        sessions = AttendanceService.get_active_users()
        return jsonify(attendance_sessions_schema.dump(sessions)), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Internal server error"}), 500

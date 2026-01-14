# app/routes/report_routes.py
from flask import Blueprint, request, jsonify
from app.models import AttendanceSession, User
from app.db import db
from datetime import datetime, timedelta

report_bp = Blueprint("reports", __name__)

@report_bp.route("/daily", methods=["GET"])
def daily_report():
    date_str = request.args.get("date")  # expected YYYY-MM-DD
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    start = datetime.combine(date_obj, datetime.min.time())
    end = datetime.combine(date_obj, datetime.max.time())

    sessions = AttendanceSession.query.filter(
        AttendanceSession.check_in_time >= start,
        AttendanceSession.check_in_time <= end
    ).all()

    report = [
        {
            "user_id": s.user_id,
            "user_name": s.user.name,
            "check_in": s.check_in_time,
            "check_out": s.check_out_time,
            "is_late": s.is_late,
            "duration_minutes": s.duration_minutes
        } for s in sessions
    ]
    return jsonify(report), 200

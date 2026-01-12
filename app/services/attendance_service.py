from datetime import datetime
from app.db import db
from app.models.attendance_session import AttendanceSession
from app.models.user import User

class AttendanceError(Exception):
    """Custom exception for attendance rule violations."""
    pass

class AttendanceService:

    @staticmethod
    def check_in(user_id, source="WEB"):
        """
        Allows a user to check in.
        Enforces that only one active session exists.
        """
        # Fetch user
        user = User.query.get(user_id)
        if not user or not user.is_active:
            raise AttendanceError("User does not exist or is inactive.")

        # Check for active session
        active_session = AttendanceSession.query.filter_by(
            user_id=user_id, status="ACTIVE"
        ).first()
        if active_session:
            raise AttendanceError("User already has an active session.")

        # Create new session
        session = AttendanceSession(
            user_id=user_id,
            check_in_time=datetime.utcnow(),
            status="ACTIVE",
            source=source
        )
        db.session.add(session)
        db.session.commit()
        return session

    @staticmethod
    def check_out(user_id):
        """
        Allows a user to check out.
        Closes the active session.
        """
        # Fetch user
        user = User.query.get(user_id)
        if not user or not user.is_active:
            raise AttendanceError("User does not exist or is inactive.")

        # Find active session
        active_session = AttendanceSession.query.filter_by(
            user_id=user_id, status="ACTIVE"
        ).first()
        if not active_session:
            raise AttendanceError("No active session found for check-out.")

        # Close session
        active_session.check_out_time = datetime.utcnow()
        active_session.status = "CLOSED"

        db.session.commit()
        return active_session

    @staticmethod
    def get_user_history(user_id):
        """
        Returns all attendance sessions for a user, newest first.
        """
        user = User.query.get(user_id)
        if not user:
            raise AttendanceError("User does not exist.")

        sessions = AttendanceSession.query.filter_by(
            user_id=user_id
        ).order_by(AttendanceSession.check_in_time.desc()).all()

        return sessions

    @staticmethod
    def get_active_users():
        """
        Returns all users currently checked in.
        """
        return AttendanceSession.query.filter_by(status="ACTIVE").all()

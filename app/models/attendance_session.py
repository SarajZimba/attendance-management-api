from datetime import datetime
from app.db import db


class AttendanceSession(db.Model):
    __tablename__ = "attendance_sessions"

    id = db.Column(db.BigInteger, primary_key=True)

    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    check_in_time = db.Column(
        db.DateTime,
        nullable=False
    )

    check_out_time = db.Column(
        db.DateTime,
        nullable=True
    )

    status = db.Column(
        db.Enum("ACTIVE", "CLOSED", name="attendance_status"),
        nullable=False,
        default="ACTIVE"
    )

    source = db.Column(
        db.Enum("WEB", "MOBILE", name="attendance_source"),
        nullable=False,
        default="WEB"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationship
    user = db.relationship(
        "User",
        back_populates="attendance_sessions"
    )

    is_late = db.Column(db.Boolean, default=False)

    duration_minutes = db.Column(db.Integer)

# ✅ New test column
    test_column = db.Column(db.String(50), default="Test")
    def __repr__(self):
        return (
            f"<AttendanceSession id={self.id} "
            f"user_id={self.user_id} status={self.status}>"
        )

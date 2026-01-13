# app/services/user_service.py
from app.models.user import User
from app.db import db
from werkzeug.security import generate_password_hash
class UserError(Exception):
    pass

class UserService:

    @staticmethod
    def create_user(name, email, password, role="USER"):
        if User.query.filter_by(email=email).first():
            raise UserError("Email already exists")
        password_hash = generate_password_hash(password)  # hash password
        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
            role=role
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        if not user:
            raise UserError("User not found")
        return user

    @staticmethod
    def deactivate_user(user_id):
        user = UserService.get_user_by_id(user_id)
        user.is_active = False
        db.session.commit()
        return user

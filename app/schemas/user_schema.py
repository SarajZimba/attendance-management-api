# app/schemas/user_schema.py
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    role = fields.Str()
    is_active = fields.Bool()
    created_at = fields.DateTime(dump_only=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

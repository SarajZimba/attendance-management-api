from marshmallow import Schema, fields, validate

class CheckInSchema(Schema):
    user_id = fields.Int(required=True)
    source = fields.Str(
        required=False,
        validate=validate.OneOf(["WEB", "MOBILE"]),
        load_default="WEB"
    )

class CheckOutSchema(Schema):
    user_id = fields.Int(required=True)

class AttendanceSessionSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    check_in_time = fields.DateTime()
    check_out_time = fields.DateTime(allow_none=True)
    status = fields.Str()
    source = fields.Str()
    created_at = fields.DateTime()

# Native Imports
from marshmallow import Schema, fields


# Created Imports


class UserSchema(Schema):
    user_id = fields.Integer()
    user_name = fields.String()
    user_password = fields.String()
    user_email = fields.String()
    user_token = fields.String()
    user_status = fields.Integer()


class UserBasicSchema(Schema):
    user_id = fields.Integer()
    user_name = fields.String()
    user_email = fields.String()
    user_status = fields.Integer()
    user_last_modification_user_id = fields.Integer()

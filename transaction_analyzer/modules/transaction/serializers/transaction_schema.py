# Native Imports
from marshmallow import Schema, fields

# Created Imports
from modules.users.serializers.user_seriallizer import UserBasicSchema


class TransactionSchema(Schema):
    transaction_id = fields.Integer()
    transaction_home_bank = fields.String()
    transaction_home_branch = fields.Integer()
    transaction_home_account = fields.String()
    transaction_destination_bank = fields.String()
    transaction_destination_branch = fields.Integer()
    transaction_destination_account = fields.String()
    transaction_amount = fields.Float()
    transaction_date_time = fields.DateTime()

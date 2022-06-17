from jsonschema import validate

json_transaction = {
    'type': 'array',
    'items': {
        'type': 'object',
        'required': [
            'transaction_home_bank',
            'transaction_home_branch',
            'transaction_home_account',
            'transaction_destination_bank',
            'transaction_destination_branch',
            'transaction_destination_account',
            'transaction_amount',
            'transaction_date_time',
        ],
        'properties': {
            'transaction_home_bank': {'type': 'string', 'minLength': 1},
            'transaction_home_branch': {'type': 'integer'},
            'transaction_home_account': {'type': 'string', 'minLength': 1},
            'transaction_destination_bank': {'type': 'string', 'minLength': 1},
            'transaction_destination_branch': {'type': 'integer'},
            'transaction_destination_account': {
                'type': 'string',
                'minLength': 1,
            },
            'transaction_amount': {'type': 'number'},
            'transaction_date_time': {'type': 'string', 'format': 'date-time'},
        },
    },
}


def json_validate_transaction(json):
    try:
        validate(json, json_transaction)
    except:
        return False
    return True

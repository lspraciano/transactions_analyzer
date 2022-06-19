from jsonschema import validate

json_user_update = {
    'title': 'user_update',
    'type': 'object',
    'required': ['user_id', 'user_name', 'user_email', 'user_status'],
    'properties': {
        'user_id': {'type': 'integer', 'minimum': 1},
        'user_name': {'type': ['string', 'null'], 'minLength': 1},
        'user_email': {'type': ['string', 'null'], 'minLength': 1},
        'user_status': {'type': ['integer', 'null'], 'enum': [0, 1, None]},
    },
}


def json_validate_update_user(json):
    try:
        validate(json, json_user_update)
    except:
        return False
    return True

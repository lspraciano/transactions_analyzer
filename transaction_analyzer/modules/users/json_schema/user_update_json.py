from jsonschema import validate

json_user_update = {
    'title': 'user_update',
    'type': 'object',
    'required': ['user_id', 'user_name', 'user_email', 'user_status'],
    'properties': {
        'user_id': {'type': 'integer'},
        'user_name': {'type': ['string', 'null']},
        'user_email': {'type': ['string', 'null']},
        'user_status': {'type': 'integer', 'enum': [0, 1]},
    },
}


def json_validate_update_user(json):
    try:
        validate(json, json_user_update)
    except:
        return False
    return True

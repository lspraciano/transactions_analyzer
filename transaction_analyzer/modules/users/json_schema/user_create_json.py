from jsonschema import validate

json_user_create = {
    'title': 'user_create',
    'type': 'object',
    'required': ['user_name', 'user_email'],
    'properties': {
        'user_name': {'type': 'string', 'minLength': 1},
        'user_email': {'type': 'string', 'minLength': 1},
    },
}


def json_validate_create_user(json):
    try:
        validate(json, json_user_create)
    except:
        return False
    return True

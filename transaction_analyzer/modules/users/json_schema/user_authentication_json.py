from jsonschema import validate

json_user_authentication = {
    'title': 'user_authentication',
    'type': 'object',
    'required': ['user_name', 'user_password'],
    'properties': {
        'user_name': {'type': 'string', 'minLength': 1},
        'user_password': {'type': 'string', 'minLength': 1},
    },
}


def json_validate_user_authentication(json):
    try:
        validate(json, json_user_authentication)
    except:
        return False
    return True

from jsonschema import validate

json_user_password_update = {
    'title': 'json_user_password_update',
    'type': 'object',
    'required': ['user_id', 'user_password', 'user_token'],
    'properties': {
        'user_id': {'type': 'integer'},
        'user_password': {'type': 'string', 'minLength': 8},
        'user_token': {
            'type': 'integer',
            'minimum': 100000,
            'maximum': 999999,
        },
    },
}


def json_validate_user_password_update(json):
    try:
        validate(json, json_user_password_update)
    except:
        return False
    return True

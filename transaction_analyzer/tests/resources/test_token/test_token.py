# Imports Native
import jwt

# Created Imports
from resources.py.token.token_manager import (
    token_generator,
    token_authentication,
    user_id_from_token,
    mail_token_generate,
)


def test_token_generator_with_valid_parameter_int(app):
    expected_user_id = 1
    dict_token_jwt = token_generator(user_id=expected_user_id)
    token_from_dict = dict_token_jwt['token']
    decode = jwt.decode(
        token_from_dict, app.config['SECRET_KEY'], algorithms=['HS256']
    )
    assert expected_user_id == decode['id']


def test_token_generator_with_invalid_parameter_str(app):
    expected_user_id = '1'
    dict_token_jwt = token_generator(user_id=expected_user_id)
    if 'error' in dict_token_jwt:
        assert True
    else:
        assert False


def test_token_generator_with_invalid_parameter_float(app):
    expected_user_id = 1.5
    dict_token_jwt = token_generator(user_id=expected_user_id)
    if 'error' in dict_token_jwt:
        assert True
    else:
        assert False


def test_token_generator_with_invalid_parameter_none(app):
    expected_user_id = None
    dict_token_jwt = token_generator(user_id=expected_user_id)
    if 'error' in dict_token_jwt:
        assert True
    else:
        assert False


def test_token_authentication_in_fake_route_with_valid_token(app, client):
    with app.app_context():
        dict_token_jwt = token_generator(user_id=1)
        token_from_dict = dict_token_jwt['token']
        cookie_name = app.config['TOKEN_NAME']

        @app.route('/fake_token_authentication')
        @token_authentication
        def fake_route_token_authentication():
            return {'success': 'ok'}, 200

        client.set_cookie('localhost', cookie_name, token_from_dict)
        response = client.get('/fake_token_authentication')

        assert response.status_code == 200
        assert 'success' in response.json


def test_token_authentication_in_fake_route_with_invalid_token_name(
    app, client
):
    with app.app_context():
        dict_token_jwt = token_generator(user_id=1)
        token_from_dict = dict_token_jwt['token']
        cookie_name = 'foo'

        client.set_cookie('localhost', cookie_name, token_from_dict)
        response = client.get('/fake_token_authentication')

        assert response.status_code == 401
        assert 'error' in response.json


def test_token_authentication_in_fake_route_with_invalid_token_value(
    app, client
):
    with app.app_context():
        token_from_dict = 'foo'
        cookie_name = app.config['TOKEN_NAME']

        client.set_cookie('localhost', cookie_name, token_from_dict)
        response = client.get('/fake_token_authentication')

        assert response.status_code == 401
        assert 'error' in response.json


def test_user_id_from_token_valid_request(app, client):
    with app.app_context():
        user_id_expected = 1
        dict_token_jwt = token_generator(user_id=user_id_expected)
        token_from_dict = dict_token_jwt['token']
        cookie_name = app.config['TOKEN_NAME']

        @app.route('/fake_token_from_token')
        def fake_route_token_from_token():
            user_id = user_id_from_token()
            return user_id

        client.set_cookie('localhost', cookie_name, token_from_dict)
        response = client.get('/fake_token_from_token')

        assert response.status_code == 200
        assert user_id_expected == response.json['user_id']


def test_user_id_from_token_invalid_token_name(app, client):
    with app.app_context():
        user_id_expected = 1
        dict_token_jwt = token_generator(user_id=user_id_expected)
        token_from_dict = dict_token_jwt['token']
        cookie_name = 'foo'

        client.set_cookie('localhost', cookie_name, token_from_dict)
        response = client.get('/fake_token_from_token')

        assert response.status_code == 200
        assert 'error' in response.json


def test_user_id_from_token_invalid_token_value(app, client):
    with app.app_context():
        token_from_dict = 'foo'
        cookie_name = app.config['TOKEN_NAME']

        client.set_cookie('localhost', cookie_name, token_from_dict)
        response = client.get('/fake_token_from_token')

        assert response.status_code == 200
        assert 'error' in response.json


def test_mail_token_generate_valid_call():
    mail_token = mail_token_generate()
    assert type(mail_token) is int
    assert 100000 < mail_token < 999999

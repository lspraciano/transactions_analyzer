# Imports Native
import pytest
from flask import template_rendered

# Created Imports
from transaction_analyzer.database.database import create_session
from transaction_analyzer.resources.py.token.token_manager import token_generator
from run import run_server


@pytest.fixture(scope='module')
def app():
    """
    Esta função retorna uma instancia do app flask

    :return: app flask
    """
    app = run_server()
    return app


@pytest.fixture(scope='function')
def client(app):
    """
    Esta função retorna um cliente HTTP para ser usado durante os teste desta aplicação. Este cliente NÃO
    POSSUI o TOKEN JWT adicionado nos cookies

    :param app: app flask
    :return: client HTTP
    """
    return app.test_client()


@pytest.fixture(scope='function')
def token_jwt_admin_user(app):
    """
    Esta função retorna TOKEN JWT com payload para o usuário administrador

    :param app: app flask
    :return: client HTTP
    """

    token_not_bearer = str(token_generator(app.config['ADMIN_USER_ID'])['token'])
    token_bearer = 'Bearer ' + token_not_bearer
    return token_bearer


@pytest.fixture(scope='function')
def session(app):
    """
    Esta função retorna uma sessão do SQLAlchemy

    :param app: app flask
    :return: session
    """
    with app.app_context():
        return create_session()


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

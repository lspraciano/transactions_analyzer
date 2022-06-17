# Imports Native
from sqlalchemy_utils import database_exists

# Created Imports
from database.database import create_session
from modules.users.models.user_model import User

session = create_session()


def test_db_is_on_test(app):
    assert 'test' in app.config['SQLALCHEMY_DATABASE_URI']


def test_db_is_created(app):
    assert database_exists(app.config['SQLALCHEMY_DATABASE_URI'])


def test_user_admin_is_created(app):
    user = (
        session.query(User)
        .filter_by(user_name=app.config['ADMIN_USER_NAME'])
        .first()
    )
    session.close()
    assert user is not None

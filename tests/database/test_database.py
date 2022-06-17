# Imports Native


# Created Imports
from transaction_analyzer.database.database import create_session
from transaction_analyzer.modules.users.models.user_model import User

session = create_session()


def test_user_admin_is_created(app):
    user = (
        session.query(User)
        .filter_by(user_name=app.config['ADMIN_USER_NAME'])
        .first()
    )
    session.close()
    assert user is not None

# Native Imports
from flask import Flask
from flask_mail import Mail

# BluePrints Imports
from database.database import create_db
from modules.home.home import home_blueprint
from modules.root.root import root_blueprint
from modules.transaction.transaction import transaction_blueprint
from resources.resources import resources_blueprint
from modules.users.user import user_blueprint


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    _register_extensions(app)
    _register_blueprint(app)
    create_db(app)

    return app


def _register_extensions(app: Flask) -> None:
    Mail(app)


def _register_blueprint(app: Flask) -> None:
    app.register_blueprint(root_blueprint, url_prefix='/')
    app.register_blueprint(home_blueprint, url_prefix='/home')
    app.register_blueprint(transaction_blueprint, url_prefix='/transaction')
    app.register_blueprint(resources_blueprint, url_prefix='/resources')
    app.register_blueprint(user_blueprint, url_prefix='/user')

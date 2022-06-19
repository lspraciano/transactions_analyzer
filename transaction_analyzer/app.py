# Native Imports
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail

# BluePrints Imports
from transaction_analyzer.database.database import create_db
from transaction_analyzer.modules.home.home import home_blueprint
from transaction_analyzer.modules.root.root import root_blueprint
from transaction_analyzer.modules.transaction.transaction import transaction_blueprint
from transaction_analyzer.resources.resources import resources_blueprint
from transaction_analyzer.modules.users.user import user_blueprint


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    _register_extensions(app)
    _register_blueprint(app)
    create_db(app)

    return app


def _enable_cors(app: Flask) -> None:
    CORS(app)


def _register_extensions(app: Flask) -> None:
    Mail(app)


def _register_blueprint(app: Flask) -> None:
    app.register_blueprint(root_blueprint, url_prefix='/')
    app.register_blueprint(home_blueprint, url_prefix='/home')
    app.register_blueprint(transaction_blueprint, url_prefix='/transaction')
    app.register_blueprint(resources_blueprint, url_prefix='/resources')
    app.register_blueprint(user_blueprint, url_prefix='/user')

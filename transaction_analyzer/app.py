# Native Imports
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_swagger_ui import get_swaggerui_blueprint

# BluePrints Imports
from transaction_analyzer.database.database import create_db
from transaction_analyzer.modules.home.home import home_blueprint
from transaction_analyzer.modules.root.root import root_blueprint
from transaction_analyzer.modules.transaction.transaction import transaction_blueprint
from transaction_analyzer.resources.resources import resources_blueprint
from transaction_analyzer.modules.users.user import user_blueprint
from docs.docs import docs_blueprint


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    _register_extensions(app)
    _register_blueprint(app)
    _register_swagger_ui(app)
    _enable_cors(app)
    create_db(app)

    return app


def _enable_cors(app: Flask) -> None:
    CORS(app)


def _register_swagger_ui(app: Flask) -> None:
    swagger_blueprint = get_swaggerui_blueprint(
        app.config['SWAGGER_URL'],
        app.config['API_URL'],
    )
    app.register_blueprint(swagger_blueprint, url_prefix=app.config['SWAGGER_URL'])


def _register_extensions(app: Flask) -> None:
    Mail(app)


def _register_blueprint(app: Flask) -> None:
    app.register_blueprint(root_blueprint, url_prefix='/')
    app.register_blueprint(home_blueprint, url_prefix='/home')
    app.register_blueprint(transaction_blueprint, url_prefix='/transaction')
    app.register_blueprint(resources_blueprint, url_prefix='/resources')
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(docs_blueprint, url_prefix='/docs')

import os
import sys

from dotenv import load_dotenv

load_dotenv()


class Configuration:
    HOST = '0.0.0.0'
    PORT = 5001
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
    ADMIN_USER_ID = 1  # System user admin ID
    ADMIN_USER_NAME = 'ADMIN'  # System user admin name
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')  # System user admin password
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')  # System user admin email
    ADMIN_STATUS = 1  # System user admin status
    TIME_EXP_TOKEN = 30  # Time in minutes of JWT token
    LIMIT_EXP_TOKEN = 1  # Time in minutes of JWT token to expire
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    SWAGGER = {
        'title': 'Transactions Analyzer - API',
        "version": "1.0.0",
        "contact": {
            "name": "Suporte a Desenvolvedores",
            "email": "luskcct@gmail.com"
        },
        "license": {
            "name": "Licença GPLv3",
            "url": "https://www.gnu.org/licenses/gpl-3.0.html"
        },
        'uiversion': 3,
        'openapi': '3.0.3',
        'persistAuthorization': True,
    }


class DevelopmentConfig(Configuration):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_SQLALCHEMY_DATABASE_URI')
    DEBUG = True


class TestConfig(Configuration):
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_SQLALCHEMY_DATABASE_URI')
    MAIL_SUPPRESS_SEND = True  # Suppress sending email
    DEBUG = False
    TESTING = True


class ProductionConfig(Configuration):
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_SQLALCHEMY_DATABASE_URI')
    DEBUG = False


app_configuration = {
    'development': DevelopmentConfig(),
    'test': TestConfig(),
    'production': ProductionConfig(),
    'default': ProductionConfig(),
}

app_active = os.getenv('FLASK_ENV') or 'default'

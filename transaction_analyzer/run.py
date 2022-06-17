# Native Imports
import sys
from importlib import reload

# Created Imports
from app import create_app
from configuration.configuration import app_configuration, app_active

if __name__ == '__main__':
    config = app_configuration[app_active]
    app = create_app(config)
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG'],
    )
    reload(sys)


def run_server():
    config_server = app_configuration[app_active]
    server = create_app(config_server)
    return server

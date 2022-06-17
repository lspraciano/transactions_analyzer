from flask import Blueprint

resources_blueprint = Blueprint(
    'resource', __name__, template_folder='templates', static_folder='/'
)

# Native Imports
from flask import Blueprint

docs_blueprint = Blueprint('docs', __name__, template_folder='templates', static_folder='/')

# Native Imports
from flask import Blueprint, render_template


home_blueprint = Blueprint(
    'home', __name__, template_folder='templates', static_folder='static'
)


@home_blueprint.route('/')
def home_page():
    return render_template('home.html'), 200


@home_blueprint.route('/dashboard')
def get_dashboards():
    return render_template('dashboards.html'), 200

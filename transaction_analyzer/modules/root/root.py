# Native Imports
from flask import Blueprint, redirect, url_for

root_blueprint = Blueprint('root', __name__)


@root_blueprint.route('/')
def redirect_to_login():
    return redirect(url_for('user.user_authentication'))


@root_blueprint.route('/logout')
def logout():
    return redirect(url_for('user.user_authentication'))

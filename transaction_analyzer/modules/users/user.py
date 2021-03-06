# Native Imports
from flask import Blueprint, render_template, request

# Created Imports
from flask_cors import cross_origin

from transaction_analyzer.modules.users.controllers.user_controller import (
    check_login_password,
    get_all_users,
    create_new_user,
    update_user,
    send_reset_password_token_to_user,
    user_update_password_by_token_and_id,
)
from transaction_analyzer.resources.py.token.token_manager import token_authentication

user_blueprint = Blueprint(
    'user', __name__, template_folder='templates', static_folder='static'
)


@user_blueprint.route('/login', methods=['GET'])
def user_template_login():
    return render_template('user_authentication.html')


@user_blueprint.route('/manager-template', methods=['GET'])
def user_template_manager():
    return render_template('user_manager.html')


@user_blueprint.route('/password-reset-template', methods=['GET'])
@cross_origin()
def user_template_reset_password():
    return render_template('user_password_recovery.html')


@user_blueprint.route('/', methods=['GET', 'POST', 'PATCH'])
@cross_origin()
@token_authentication
def user():
    if request.method == 'GET':
        return get_all_users()
    elif request.method == 'POST':
        created_user = create_new_user(request.json)
        return created_user
    elif request.method == 'PATCH':
        return update_user(request.json)


@user_blueprint.route('/authentication', methods=['POST'])
@cross_origin()
def user_authentication():
    return check_login_password(request.json)


@user_blueprint.route('/reset-password', methods=['POST', 'PATCH'])
@cross_origin()
def user_reset_password():
    if request.method == 'POST':
        return send_reset_password_token_to_user(request.json)
    elif request.method == 'PATCH':
        return user_update_password_by_token_and_id(request.json)

# Native Imports
import datetime

from flask import Blueprint, render_template, request

# Created Imports
from flask_cors import cross_origin

from transaction_analyzer.modules.transaction.controllers.transaction_controller import (
    save_transactions_list,
    get_transactions_list_by_date,
    get_suspects_transactions_report,
    get_transactions_report,
)
from transaction_analyzer.modules.transaction.controllers.transaction_log_controller import (
    get_all_logs,
)
from transaction_analyzer.resources.py.token.token_manager import token_authentication

transaction_blueprint = Blueprint(
    'transaction',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@transaction_blueprint.route('/transaction-import-template', methods=['GET'])
def template_import_csv():
    return render_template('import_transaction.html')


@transaction_blueprint.route('/transaction-log-template', methods=['GET'])
def template_audit_transaction():
    return render_template('transaction_log.html')


@transaction_blueprint.route('/transaction-suspect-template', methods=['GET'])
def template_transactions_suspect():
    return render_template('suspects_transaction.html')


@transaction_blueprint.route('/', methods=['GET', 'POST'])
@cross_origin()
@token_authentication
def transactions():
    if request.method == 'GET':
        return get_transactions_list_by_date(request)
    elif request.method == 'POST':
        return save_transactions_list(request.json)


@transaction_blueprint.route('/log/get-log', methods=['GET'])
@cross_origin()
@token_authentication
def audit_transaction_data():
    return get_all_logs(), 200


@transaction_blueprint.route('/suspect', methods=['GET'])
@cross_origin()
@token_authentication
def transactions_suspect():
    return get_suspects_transactions_report(request)


@transaction_blueprint.route('/report', methods=['GET'])
@cross_origin()
@token_authentication
def transactions_report():
    return get_transactions_report()

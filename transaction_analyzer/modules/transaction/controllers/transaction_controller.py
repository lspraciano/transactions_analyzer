# Native Imports
from datetime import datetime
from flask import request, make_response
from sqlalchemy import extract, func

# Created Imports
from database.database import create_session
from error.error import get_error_msg
from modules.transaction.controllers.transaction_log_controller import (
    save_transaction_log,
)
from modules.transaction.json_schema.transactions_json import (
    json_validate_transaction,
)
from modules.transaction.models.transaction_model import Transaction
from modules.transaction.serializers.transaction_schema import (
    TransactionSchema,
)

session = create_session()
TransactionSchema = TransactionSchema(many=True)


def get_transaction_by_date(transactions_date: datetime) -> dict:
    """
    Esta função retona uma lista de diocnário contendo as transações referentes a data informada.

    :param transactions_date: data da(s) transação(ões)
    :return: [ { transações } ]
    """
    if not isinstance(transactions_date, datetime):
        return {'error': 'invalid date'}

    transactions = (
        session.query(Transaction)
        .filter(
            extract('month', Transaction.transaction_date_time)
            == transactions_date.month,
            extract('year', Transaction.transaction_date_time)
            == transactions_date.year,
            extract('day', Transaction.transaction_date_time)
            == transactions_date.day,
        )
        .all()
    )

    session.close()

    return {'transactions': TransactionSchema.dump(transactions)}


def validate_transaction_list(transactions_list: list) -> dict:
    """
    Essa função é responsável por realizar a validação da lista de transações recebidas. Se a lista for
    considerada válida, será retornado {'success': 'ok'}, caso contrário {'error': 'foo'}. A formatação da lista deve
    seguir esta ordem de valores:[ { "transaction_home_bank" : "type": "string", "transaction_home_branch" : "type":
    "integer", "transaction_home_account" : "type": "string", "transaction_destination_bank" : "type": "string",
    "transaction_destination_branch" : "type": "integer", "transaction_destination_account" : "type": "string",
    "transaction_amount" : "type": "number", "transaction_date_time" : "type": "string" }, ]



    :param transactions_list: lista de transações
    :return: em caso de sucesso será retornado {'success': 'ok'} ou em caso de não sucesso
     { 'error': foo }
    """
    try:
        if not json_validate_transaction(transactions_list):
            return {'error': 'invalid json'}

        transactions_date = datetime.strptime(
            transactions_list[0]['transaction_date_time'], '%Y-%m-%dT%H:%M:%S'
        )
        check_transactions_existence_in_db = get_transaction_by_date(
            transactions_date
        )
        if check_transactions_existence_in_db['transactions']:
            return {'error': 'file with this date already exists'}

        for transaction in transactions_list:
            current_transaction_date = datetime.strptime(
                transaction['transaction_date_time'], '%Y-%m-%dT%H:%M:%S'
            )
            if (
                current_transaction_date.date() != transactions_date.date()
                or '' in transaction.values()
            ):
                return {'error': 'there are records other than the file date'}

        return {'success': 'ok'}
    except:
        return get_error_msg()


def get_transactions_list_by_date(
    transaction_request: request,
) -> make_response:
    """
    Esta função retorna um dicionário contendo todas as transações para uma determinada data. A data deve ser informada
    como parâmentro de entrada no formato datetime.

    :param transaction_request: requisição do usuário
    :return: em caso de sucesso será retornado {'transactions': [ { transações }, ]  ou em caso de erro inesperado
     { 'error' : foo }
    """

    try:
        transactions_date = transaction_request.args.get('date')

        try:
            transactions_date = datetime.strptime(
                transactions_date, '%d/%m/%Y'
            )
        except:
            return make_response({'error': 'invalid date'}, 400)

        transactions = get_transaction_by_date(transactions_date)

        if 'error' in transactions.keys():
            return make_response(transactions, 400)
        return make_response(transactions, 200)

    except:
        return get_error_msg()


def save_transactions_list(transactions_list: list) -> make_response:
    """
    Esta função salva uma lista de transações no banco de dados.  A formatação da lista de dicionário deve seguir
    esta ordem de valores: { "transaction_home_bank" : "type": "string", "transaction_home_branch" : "type": "integer",
    "transaction_home_account" : "type": "string", "transaction_destination_bank" : "type": "string",
    "transaction_destination_branch" : "type": "integer", "transaction_destination_account" : "type": "string",
    "transaction_amount" : "type": "number", "transaction_date_time" : "type": "string" }

    :param transactions_list: lista de transações
    :return: no caso de sucesso: { 'success': { 'transactions': número de linhas } } ou em caso de NÃO sucesso
     { 'error': foo }
    """

    try:
        check_transactions = validate_transaction_list(transactions_list)

        if 'error' in check_transactions:
            return make_response(check_transactions, 400)

        transactions = []
        transaction_date = ''

        for transaction in transactions_list:
            transaction_date = datetime.strptime(
                transaction['transaction_date_time'], '%Y-%m-%dT%H:%M:%S'
            )
            row = Transaction(
                transaction_home_bank=transaction['transaction_home_bank'],
                transaction_home_branch=transaction['transaction_home_branch'],
                transaction_home_account=transaction[
                    'transaction_home_account'
                ],
                transaction_destination_bank=transaction[
                    'transaction_destination_bank'
                ],
                transaction_destination_branch=transaction[
                    'transaction_destination_branch'
                ],
                transaction_destination_account=transaction[
                    'transaction_destination_account'
                ],
                transaction_amount=transaction['transaction_amount'],
                transaction_date_time=transaction_date,
            )
            transactions.append(row)

        transaction_log = save_transaction_log(transaction_date)

        if 'success' not in transaction_log.keys():
            session.rollback()
            return make_response({'error': transaction_log}, 400)

        session.add_all(transactions)
        session.commit()
        session.close()
        return make_response(
            {'success': {'transactions': len(transactions)}}, 201
        )

    except:
        session.rollback()
        return get_error_msg()


def get_suspects_transactions_report(
    suspect_request: request,
) -> make_response:
    """
    Esta função retorna um dicionário contendo as transações, agências e bancos suspeitos. Os valores que
    definem quem são ou não suspeitos são denifinidos dentro desta função.

    :param suspect_request: data referente ao mês investigado
    :return: em caso de sucesso, será retornado um dicionário com esta formatação:
            { 'transactions_suspect': [ foo ],
            'transactions_suspect_home_account': [ boo ],
            'transactions_suspect_destination_account': [ poo ],
            'transactions_suspect_home_branch': [ loo ],
            'transactions_suspect_destination_branch': [ too ] }
            --  em caso de error retornado um dicionário {'error': foo }
    """
    try:

        try:
            suspect_date = suspect_request.args.get('date')
            suspect_date = datetime.strptime(suspect_date, '%d/%m/%Y')
        except:
            return make_response({'error': 'invalid date'}, 400)

        alert_value_for_transaction = 100000
        alert_value_for_account = 700000
        alert_value_for_branch = 4900000

        transactions_suspect = (
            session.query(Transaction)
            .filter(
                extract('month', Transaction.transaction_date_time)
                == suspect_date.month,
                extract('year', Transaction.transaction_date_time)
                == suspect_date.year,
                Transaction.transaction_amount >= alert_value_for_transaction,
            )
            .all()
        )

        transactions_suspect_home_account = (
            session.query(
                Transaction.transaction_home_bank,
                Transaction.transaction_home_branch,
                Transaction.transaction_home_account,
                func.sum(Transaction.transaction_amount).label(
                    'transaction_amount'
                ),
            )
            .filter(
                extract('month', Transaction.transaction_date_time)
                == suspect_date.month,
                extract('year', Transaction.transaction_date_time)
                == suspect_date.year,
            )
            .group_by(
                Transaction.transaction_home_bank,
                Transaction.transaction_home_branch,
                Transaction.transaction_home_account,
            )
            .having(
                func.sum(Transaction.transaction_amount)
                >= alert_value_for_account
            )
            .all()
        )

        transactions_suspect_destination_account = (
            session.query(
                Transaction.transaction_destination_bank,
                Transaction.transaction_destination_branch,
                Transaction.transaction_destination_account,
                func.sum(Transaction.transaction_amount).label(
                    'transaction_amount'
                ),
            )
            .filter(
                extract('month', Transaction.transaction_date_time)
                == suspect_date.month,
                extract('year', Transaction.transaction_date_time)
                == suspect_date.year,
            )
            .group_by(
                Transaction.transaction_destination_bank,
                Transaction.transaction_destination_branch,
                Transaction.transaction_destination_account,
            )
            .having(
                func.sum(Transaction.transaction_amount)
                >= alert_value_for_account
            )
            .all()
        )

        transactions_suspect_home_branch = (
            session.query(
                Transaction.transaction_home_bank,
                Transaction.transaction_home_branch,
                func.sum(Transaction.transaction_amount).label(
                    'transaction_amount'
                ),
            )
            .filter(
                extract('month', Transaction.transaction_date_time)
                == suspect_date.month,
                extract('year', Transaction.transaction_date_time)
                == suspect_date.year,
            )
            .group_by(
                Transaction.transaction_home_bank,
                Transaction.transaction_home_branch,
            )
            .having(
                func.sum(Transaction.transaction_amount)
                >= alert_value_for_branch
            )
            .all()
        )

        transactions_suspect_destination_branch = (
            session.query(
                Transaction.transaction_destination_bank,
                Transaction.transaction_destination_branch,
                func.sum(Transaction.transaction_amount).label(
                    'transaction_amount'
                ),
            )
            .filter(
                extract('month', Transaction.transaction_date_time)
                == suspect_date.month,
                extract('year', Transaction.transaction_date_time)
                == suspect_date.year,
            )
            .group_by(
                Transaction.transaction_destination_bank,
                Transaction.transaction_destination_branch,
            )
            .having(
                func.sum(Transaction.transaction_amount)
                >= alert_value_for_branch
            )
            .all()
        )

        session.close()

        return {
            'transactions_suspect': TransactionSchema.dump(
                transactions_suspect
            ),
            'transactions_suspect_home_account': TransactionSchema.dump(
                transactions_suspect_home_account
            ),
            'transactions_suspect_destination_account': TransactionSchema.dump(
                transactions_suspect_destination_account
            ),
            'transactions_suspect_home_branch': TransactionSchema.dump(
                transactions_suspect_home_branch
            ),
            'transactions_suspect_destination_branch': TransactionSchema.dump(
                transactions_suspect_destination_branch
            ),
        }, 200
    except:
        return make_response(get_error_msg(), 400)


def get_transactions_report() -> make_response:
    """
    Esta função retorna um relatório geral contendo informações básicas sobre as transações importadas.
    O relatório filtra as informações de acordo com mês corrente.

    :return:
    """
    now = datetime.now()
    rows_transactions = (
        session.query(Transaction)
        .filter(
            extract('month', Transaction.transaction_date_time) == now.month,
            extract('year', Transaction.transaction_date_time) == now.year,
        )
        .all()
    )
    session.close()

    transactions_total = len(rows_transactions)
    transactions_amount_total = 0.0
    transactions_amount_mean = 0.0
    transactions_suspect_total = 0.0
    transactions_suspect_amount_total = 0.0
    transactions_suspect_mean = 0.0
    transactions_suspect_percentage = 0.0

    for r in rows_transactions:
        transactions_amount_total += r.transaction_amount

        if r.transaction_amount >= 100000:
            transactions_suspect_total += 1
            transactions_suspect_amount_total += r.transaction_amount

    if transactions_total > 0:
        transactions_amount_mean = (
            transactions_amount_total / transactions_total
        )
        transactions_suspect_percentage = (
            transactions_suspect_total / transactions_total * 100
        )

    if transactions_suspect_total > 0:
        transactions_suspect_mean = (
            transactions_suspect_amount_total / transactions_suspect_total
        )

    rows_transactions_total_per_day = (
        session.query(
            func.count(Transaction.transaction_id).label('total'),
            extract('day', Transaction.transaction_date_time).label('day'),
        )
        .filter(
            extract('month', Transaction.transaction_date_time) == now.month,
            extract('year', Transaction.transaction_date_time) == now.year,
        )
        .order_by('day')
        .group_by(extract('day', Transaction.transaction_date_time))
        .all()
    )

    session.close()

    rows_transactions_total_per_bank = (
        session.query(
            func.count(Transaction.transaction_id).label('total'),
            Transaction.transaction_home_bank,
        )
        .filter(
            extract('month', Transaction.transaction_date_time) == now.month,
            extract('year', Transaction.transaction_date_time) == now.year,
        )
        .order_by('total')
        .group_by(Transaction.transaction_home_bank)
        .all()
    )

    session.close()

    transactions_total_per_day = []
    transactions_total_per_bank = []

    for r in rows_transactions_total_per_day:
        add = {'total': r[0], 'date': f'{int(r[1])}'}
        transactions_total_per_day.append(add)

    for r in rows_transactions_total_per_bank:
        add = {'total': r[0], 'bank': r[1]}
        transactions_total_per_bank.append(add)

    return {
        'transactions_total': transactions_total,
        'transactions_amount_mean': round(transactions_amount_mean, 2),
        'transactions_suspect_mean': round(transactions_suspect_mean, 2),
        'transactions_suspect_percentage': round(
            transactions_suspect_percentage, 2
        ),
        'transactions_total_per_day': transactions_total_per_day,
        'transactions_total_per_bank': transactions_total_per_bank,
    }, 200

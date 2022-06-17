# Imports Native
from flask import json

# Created Imports
from modules.transaction.controllers.transaction_log_controller import (
    get_all_logs,
)


def test_transaction_log_template_with_valid_token(
    app, client_admin_authenticaded, captured_templates
):
    response = client_admin_authenticaded.get('transaction/log')
    template, context = captured_templates[0]

    assert response.status_code == 200
    assert len(captured_templates) == 1
    assert template.name == 'transaction_log.html'


def test_transaction_log_template_without_token(client):
    response = client.get('transaction/log')
    assert response.status_code == 401


def test_save_transaction_log_with_valid_json(app, client_admin_authenticaded):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': 2,
            'transaction_destination_account': '00214',
            'transaction_amount': 240.5,
            'transaction_date_time': '2022-05-22T06:10:45',
        },
    ]

    response = client_admin_authenticaded.post(
        'transaction/',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
    )

    transaction_logs = get_all_logs()

    assert response.status_code == 201
    assert len(transaction_logs['logs']) == len(data)
    assert 'logs' in transaction_logs
    assert (
        data[0]['transaction_date_time']
        in transaction_logs['logs'][0][
            'transactions_log_transactions_datetime'
        ]
    )
    assert (
        app.config['ADMIN_USER_ID']
        == transaction_logs['logs'][0]['transactions_log_id']
    )


def test_save_transaction_log_with_invalid_json_field_transaction_home_bank(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bankk': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': 2,
            'transaction_destination_account': '00214',
            'transaction_amount': 240.5,
            'transaction_date_time': '2022-05-23T06:10:45',
        },
    ]

    response = client_admin_authenticaded.post(
        'transaction/',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
    )

    transaction_logs = get_all_logs()

    assert response.status_code == 400
    for log in transaction_logs['logs']:
        assert (
            data[0]['transaction_date_time']
            not in log['transactions_log_transactions_datetime']
        )

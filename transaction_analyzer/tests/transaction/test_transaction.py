# Imports Native
from datetime import datetime

from flask import json

# Created Imports
from modules.transaction.controllers.transaction_controller import (
    get_transaction_by_date,
)


def test_import_transaction_template_with_valid_token(
    app, client_admin_authenticaded, captured_templates
):
    response = client_admin_authenticaded.get('transaction/import')
    template, context = captured_templates[0]

    assert response.status_code == 200
    assert len(captured_templates) == 1
    assert template.name == 'import_transaction.html'


def test_import_transaction_template_without_token(client):
    response = client.get('transaction/import')
    assert response.status_code == 401


def test_import_one_transaction_with_valid_json(
    app, client_admin_authenticaded
):
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

    transactions_by_date = get_transaction_by_date(
        datetime.strptime(
            data[0]['transaction_date_time'], '%Y-%m-%dT%H:%M:%S'
        )
    )

    assert response.status_code == 201
    assert 'success' in response.json
    assert 'transactions' in transactions_by_date
    assert len(transactions_by_date['transactions']) == len(data)
    for idx, transaction in enumerate(transactions_by_date['transactions']):
        assert (
            transaction['transaction_home_bank']
            == data[idx]['transaction_home_bank']
        )
        assert (
            transaction['transaction_home_branch']
            == data[idx]['transaction_home_branch']
        )
        assert (
            transaction['transaction_home_account']
            == data[idx]['transaction_home_account']
        )
        assert (
            transaction['transaction_destination_bank']
            == data[idx]['transaction_destination_bank']
        )
        assert (
            transaction['transaction_destination_account']
            == data[idx]['transaction_destination_account']
        )
        assert (
            transaction['transaction_amount']
            == data[idx]['transaction_amount']
        )
        assert (
            transaction['transaction_date_time']
            == data[idx]['transaction_date_time']
        )


def test_import_one_transaction_already_existing_data(
    app, client_admin_authenticaded
):
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

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_home_bank(
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
            'transaction_date_time': '2022-05-22T06:10:45',
        },
    ]

    response = client_admin_authenticaded.post(
        'transaction/',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
    )

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_home_branch(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branchh': 1,
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

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_home_account(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_accountt': '00223',
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

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_destination_bank(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bankk': 'TEST2',
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

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_destination_branch(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branchh': 2,
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

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_destination_account(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': 2,
            'transaction_destination_accountt': '00214',
            'transaction_amount': 240.5,
            'transaction_date_time': '2022-05-22T06:10:45',
        },
    ]

    response = client_admin_authenticaded.post(
        'transaction/',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
    )

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_amount(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': 2,
            'transaction_destination_account': '00214',
            'transaction_amountt': 240.5,
            'transaction_date_time': '2022-05-22T06:10:45',
        },
    ]

    response = client_admin_authenticaded.post(
        'transaction/',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
    )

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_date_time(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': 2,
            'transaction_destination_account': '00214',
            'transaction_amount': 240.5,
            'transaction_date_timee': '2022-05-22T06:10:45',
        },
    ]

    response = client_admin_authenticaded.post(
        'transaction/',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
    )

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_home_bank(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': '',
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

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_home_branch(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': '1',
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

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_home_account(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '',
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

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_destination_bank(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': '',
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

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_destination_branch(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': '2',
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

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_destination_account(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': 2,
            'transaction_destination_account': '',
            'transaction_amount': 240.5,
            'transaction_date_time': '2022-05-22T06:10:45',
        },
    ]

    response = client_admin_authenticaded.post(
        'transaction/',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
    )

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_amount(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': 2,
            'transaction_destination_account': '00214',
            'transaction_amount': '240.5',
            'transaction_date_time': '2022-05-22T06:10:45',
        },
    ]

    response = client_admin_authenticaded.post(
        'transaction/',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
    )

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_date_time(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': 2,
            'transaction_destination_account': '00214',
            'transaction_amount': 240.5,
            'transaction_date_timee': '',
        },
    ]

    response = client_admin_authenticaded.post(
        'transaction/',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
    )

    assert response.status_code == 400
    assert 'error' in response.json


def test_import_two_transactions_with_valid_json(
    app, client_admin_authenticaded
):
    data = [
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': 2,
            'transaction_destination_account': '00214',
            'transaction_amount': 240.5,
            'transaction_date_time': '2022-05-24T06:10:45',
        },
        {
            'transaction_home_bank': 'TEST',
            'transaction_home_branch': 1,
            'transaction_home_account': '00223',
            'transaction_destination_bank': 'TEST2',
            'transaction_destination_branch': 2,
            'transaction_destination_account': '00214',
            'transaction_amount': 550.5,
            'transaction_date_time': '2022-05-24T06:10:45',
        },
    ]

    response = client_admin_authenticaded.post(
        'transaction/',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
    )

    transactions_by_date = get_transaction_by_date(
        datetime.strptime(
            data[0]['transaction_date_time'], '%Y-%m-%dT%H:%M:%S'
        )
    )

    assert response.status_code == 201
    assert 'success' in response.json
    assert 'transactions' in transactions_by_date
    assert len(transactions_by_date['transactions']) == len(data)
    for idx, transaction in enumerate(transactions_by_date['transactions']):
        assert (
            transaction['transaction_home_bank']
            == data[idx]['transaction_home_bank']
        )
        assert (
            transaction['transaction_home_branch']
            == data[idx]['transaction_home_branch']
        )
        assert (
            transaction['transaction_home_account']
            == data[idx]['transaction_home_account']
        )
        assert (
            transaction['transaction_destination_bank']
            == data[idx]['transaction_destination_bank']
        )
        assert (
            transaction['transaction_destination_account']
            == data[idx]['transaction_destination_account']
        )
        assert (
            transaction['transaction_amount']
            == data[idx]['transaction_amount']
        )
        assert (
            transaction['transaction_date_time']
            == data[idx]['transaction_date_time']
        )


def test_suspect_transaction_template_with_valid_token(
    app, client_admin_authenticaded, captured_templates
):
    response = client_admin_authenticaded.get('transaction/suspect/report')
    template, context = captured_templates[0]

    assert response.status_code == 200
    assert len(captured_templates) == 1
    assert template.name == 'suspects_transaction.html'


def test_suspect_transaction_template_with_invalid_token(client):
    response = client.get('transaction/suspect/report')
    assert response.status_code == 401


def test_get_suspects_transactions_report_with_valid_token_and_date(
    app, client_admin_authenticaded
):
    response = client_admin_authenticaded.get(
        'transaction/suspect?date=01/01/2022'
    )
    assert response.status_code == 200
    assert 'transactions_suspect' in response.json
    assert 'transactions_suspect_destination_account' in response.json
    assert 'transactions_suspect_destination_branch' in response.json
    assert 'transactions_suspect_home_account' in response.json
    assert 'transactions_suspect_home_branch' in response.json


def test_get_suspects_transactions_report_with_invalid_token_and_valid_date(
    client,
):
    response = client.get('transaction/suspect?date=01/01/2022')
    assert response.status_code == 401


def test_get_suspects_transactions_report_with_valid_token_and_invalid_date_format(
    client_admin_authenticaded,
):
    response = client_admin_authenticaded.get(
        'transaction/suspect?date=01-01-2022'
    )
    assert response.status_code == 400


def test_get_suspects_transactions_report_with_invalid_token_and_date_format(
    client,
):
    response = client.get('transaction/suspect?date=01-01-2022')
    assert response.status_code == 401


def test_get_suspects_transactions_report_with_valid_token_and_invalid_parameter_datey(
    client_admin_authenticaded,
):
    response = client_admin_authenticaded.get(
        'transaction/suspect?datey=01-01-2022'
    )
    assert response.status_code == 400


def test_get_suspects_transactions_report_with_valid_token_and_invalid_date_blank(
    client_admin_authenticaded,
):
    response = client_admin_authenticaded.get('transaction/suspect?date=')
    assert response.status_code == 400


def test_get_suspects_transactions_report_with_valid_token_and_no_parameter_date(
    client_admin_authenticaded,
):
    response = client_admin_authenticaded.get('transaction/suspect')
    assert response.status_code == 400


def test_report_transaction_template_with_valid_token(
    app, client_admin_authenticaded, captured_templates
):
    response = client_admin_authenticaded.get('home/dashboard')
    template, context = captured_templates[0]

    assert response.status_code == 200
    assert len(captured_templates) == 1
    assert template.name == 'dashboards.html'


def test_report_transaction_template_with_invalid_token(client):
    response = client.get('home/dashboard')
    assert response.status_code == 401


def test_get_transactions_report_with_valid_token(
    app, client_admin_authenticaded
):
    response = client_admin_authenticaded.get('transaction/report')
    assert response.status_code == 200
    assert 'transactions_total' in response.json
    assert 'transactions_amount_mean' in response.json
    assert 'transactions_suspect_mean' in response.json
    assert 'transactions_suspect_percentage' in response.json
    assert 'transactions_total_per_day' in response.json
    assert 'transactions_total_per_bank' in response.json


def test_get_transactions_report_with_invalid_token(client):
    response = client.get('transaction/report')
    assert response.status_code == 401

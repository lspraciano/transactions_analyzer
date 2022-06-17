# Native Imports
from datetime import datetime

# Created Imports
from database.database import create_session
from error.error import get_error_msg
from modules.transaction.models.transaction_logs_model import TransactionLog
from resources.py.token.token_manager import user_id_from_token
from modules.transaction.serializers.transaction_log_schema import (
    TransactionLogSchema,
)

TransactionLogSchema = TransactionLogSchema(many=True)
session = create_session()


def save_transaction_log(log_date: datetime):
    """
    Essa função salva a data que as transações serão salvas, com intuito de gerar um log de atividade. Ela recebe a
    data que as transações foram realizadas e registra no banco SQL.

    :param log_date: data das transações
    :return: No caso de sucesso: { 'success': 'log saved' } ||| No caso de erro: { 'error': erro ocorrido }
    """

    try:

        if not isinstance(log_date, datetime):
            return {'error': 'invalid date'}

        user_from_token = user_id_from_token()

        if 'user_id' not in user_from_token:
            return user_from_token

        transaction_log = TransactionLog(
            transactions_log_transactions_datetime=log_date,
            transactions_log_datetime=datetime.now(),
            transactions_log_user_id=user_from_token['user_id'],
        )

        session.add(transaction_log)
        session.commit()
        session.close()
        return {'success': 'log saved'}

    except:
        session.rollback()
        return get_error_msg()


def get_all_logs() -> dict:
    """
    Essa função retorna o histórico das transações importadas

    :return: No caso de sucesso: { 'logs': [lista de logs]] } ||| No caso de erro: { 'error': erro ocorrido }
    """
    logs = session.query(TransactionLog).all()
    session.close()
    return {'logs': TransactionLogSchema.dump(logs)}

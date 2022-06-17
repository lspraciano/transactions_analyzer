# Native Imports
from datetime import datetime, timedelta
from sqlalchemy import extract, func, distinct

# Created Imports
from database.database import create_session
from modules.users.models.user_audit_model import UserAudit

session = create_session()


def user_token_modification_count(user_id: int) -> int:
    """
    Esta função retorna o número de vezes que foi gerado tokens para reset de senha para um determinado user_id
    nos últimos 5 minutos.

    :param user_id: id do usuário
    :return:
    """
    now = datetime.now()
    past = now - timedelta(minutes=5)
    modification_last_five_minutes = (
        session.query(func.count(distinct(UserAudit.user_audit_user_token)))
        .filter(
            UserAudit.user_audit_transaction_date_time >= past,
            UserAudit.user_audit_user_id == user_id,
        )
        .all()
    )

    count = int(modification_last_five_minutes[0][0])

    return count

# Native Imports
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    event,
    DDL,
)

# Created Imports
from sqlalchemy.orm import relationship

from database.database import ModelBase


class UserAudit(ModelBase):
    __tablename__ = 'tbusers_audit'

    user_audit_id = Column(
        Integer, primary_key=True, index=True, autoincrement=True
    )
    user_audit_user_id = Column(Integer, nullable=False)
    user_audit_user_name = Column(String, nullable=False)
    user_audit_user_password = Column(String, nullable=False)
    user_audit_user_email = Column(String, nullable=False)
    user_audit_user_token = Column(String, nullable=True)
    user_audit_user_status = Column(Integer, nullable=False)
    user_audit_last_modification_user_id = Column(
        Integer, ForeignKey('tbusers.user_id'), nullable=False
    )
    user_audit_transaction_type = Column(String, nullable=False)
    user_audit_transaction_date_time = Column(
        DateTime(timezone=False), nullable=False
    )
    user_audit_user_rl = relationship('User', lazy='joined')

    def __repr__(self) -> str:
        return (
            f'User(id={self.user_audit_id}, user_id={self.user_audit_user_id})'
        )


func = DDL(
    ' CREATE OR REPLACE FUNCTION register_users_audit() '
    'RETURNS TRIGGER AS $users_audit_trigger$'
    ' BEGIN '
    ' INSERT INTO tbusers_audit '
    ' (user_audit_user_id, '
    ' user_audit_user_name, '
    ' user_audit_user_password, '
    ' user_audit_user_email, '
    ' user_audit_user_token, '
    ' user_audit_user_status, '
    ' user_audit_last_modification_user_id, '
    ' user_audit_transaction_type, '
    ' user_audit_transaction_date_time) '
    ' VALUES '
    ' (NEW.user_id, '
    ' NEW.user_name, '
    ' NEW.user_password, '
    ' NEW.user_email, '
    ' NEW.user_token, '
    ' NEW.user_status, '
    ' NEW.user_last_modification_user_id, '
    ' TG_OP, '
    ' CURRENT_TIMESTAMP); '
    ' RETURN NULL; '
    ' END; '
    ' $users_audit_trigger$ LANGUAGE plpgsql; '
)

trigger = DDL(
    ' CREATE TRIGGER t_users_audit '
    ' AFTER INSERT OR UPDATE ON tbusers '
    ' FOR EACH ROW '
    ' EXECUTE PROCEDURE register_users_audit(); '
)

event.listen(
    UserAudit.__table__, 'after_create', func.execute_if(dialect='postgresql')
)

event.listen(
    UserAudit.__table__,
    'after_create',
    trigger.execute_if(dialect='postgresql'),
)

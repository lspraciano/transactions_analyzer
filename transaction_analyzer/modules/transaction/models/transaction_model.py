# Native Imports
from database.database import ModelBase
from sqlalchemy import Column, Integer, String, Float, DateTime


class Transaction(ModelBase):
    __tablename__ = 'tbtransactions'

    transaction_id = Column(
        Integer, primary_key=True, index=True, autoincrement=True
    )
    transaction_home_bank = Column(String, nullable=False)
    transaction_home_branch = Column(Integer, nullable=False)
    transaction_home_account = Column(String, nullable=False)
    transaction_destination_bank = Column(String, nullable=False)
    transaction_destination_branch = Column(Integer, nullable=False)
    transaction_destination_account = Column(String, nullable=True)
    transaction_amount = Column(Float, nullable=False)
    transaction_date_time = Column(DateTime, nullable=False)

    def __repr__(self) -> str:
        return str(
            {
                'transaction_id': self.transaction_id,
                'transaction_home_bank': self.transaction_home_bank,
                'transaction_destination_bank': self.transaction_destination_bank,
                'transaction_amount': self.transaction_amount,
            }
        )

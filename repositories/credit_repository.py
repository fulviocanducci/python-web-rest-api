from sqlalchemy.orm import Session
from models.credit import Credit


class CreditRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Credit).all()

    def get_by_id(self, credit_id: int):
        return self.db.query(Credit).filter(Credit.id == credit_id).first()

    def add(self, credit: Credit):
        self.db.add(credit)
        self.db.commit()
        self.db.refresh(credit)
        return credit

    def update(self, credit: Credit):
        self.db.commit()
        self.db.refresh(credit)
        return credit

    def merge(self, credit: Credit):
        self.db.merge(credit)
        self.db.commit()
        self.db.refresh(credit)
        return credit

    def delete(self, credit: Credit):
        self.db.delete(credit)
        self.db.commit()

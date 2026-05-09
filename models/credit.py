from sqlalchemy import Column, Integer, String, DateTime, func
from database.main import Base


class Credit(Base):
    __tablename__ = "credit"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    name = Column(String(50), nullable=False, name="name")
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), name="created_at"
    )

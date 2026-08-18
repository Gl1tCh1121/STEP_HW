from database import Base
from sqlalchemy import Boolean, Column, Integer, String


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    destination = Column(String(100), nullable=False)
    country = Column(String(50), nullable=False)
    days = Column(Integer, nullable=False)
    budget = Column(Integer, nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)
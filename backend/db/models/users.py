from db.connections import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .mixins import Timestamp


class User(Timestamp, Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    bio = Column(String, nullable=True)
    address = Column(Integer, ForeignKey("locations.id"), nullable=False)


from db.connections import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .mixins import Timestamp

class Location(Timestamp, Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False)
    county = Column(String, nullable=False)
    street_address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    country = Column(String, nullable=False)
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Restaurant(Base):
    __tablename__   = "restaurants"
    id              = Column(Integer, primary_key=True, index=True)
    name            = Column(String, unique=True, index=True)
    description     = Column(String)
    food_type       = Column(String)
    cost            = Column(Integer)
    location        = Column(Integer)
    has_outdoors    = Column(Boolean, default=False)
    bld             = Column(Integer)
    hours           = Column(String)
    sells_alcohol   = Column(Boolean, default=False)

class User(Base):
    __tablename__   = "users"
    id              = Column(Integer, primary_key=True, index=True)
    name            = Column(String, index=True)
    age             = Column(Integer)
    veg             = Column(Boolean, default=False)
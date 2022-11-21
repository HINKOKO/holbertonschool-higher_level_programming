#!/usr/bin/python3
"""
Improved Module that contains class definition of `City`
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State

Base = declarative_base()


class City(Base):
    """
    class State that inherits from Base
    - links to the MySQL table `states`
    - id represents a column of auto-generated,
    uniq integer, can't be null and primary key
    - name represents a column of a string 128 chars max
    can't be null
    - state_id represents column of integer, can't be null
    and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

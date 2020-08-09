#!/usr/bin/python3
""" State class module """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ State class """
    __table__name = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

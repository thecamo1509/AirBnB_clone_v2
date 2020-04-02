#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", backref='state')
    else:
        @property
        def cities(self):
            """
            cities getter
            """
            city = storage.all()
            mylist = []
            for i in city:
                if i.states_id == self.id:
                    mylist.append(i)
            return mylist

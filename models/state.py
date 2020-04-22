#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


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
            city = models.storage.all('City')
            mylist = []
            for i in city.values():
                if i.state_id == self.id:
                    mylist.append(i)
            return mylist

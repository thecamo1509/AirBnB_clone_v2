#!/usr/bin/python3
"""This is the engine used for database storage"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """
    Data engine Class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Creating the documentation
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        all
        Returns a dictionary representation of the object
        """
        result = None
        mydict = {}
        mylist = []
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            for i in classes:
                try:
                    result = self.__session.query(i).all()
                    if result is not None:
                        for j in result:
                            mylist.append(j)
                except InvalidRequestError:
                    pass
        else:
            result = self.__session.query(eval(cls)).all()
            if result is not None:
                for i in result:
                    mylist.append(i)
        return (mylist)

    def new(self, obj):
        """
        New
        """
        self.__session.add(obj)
        self.save()

    def delete(self, obj=None):
        """
        delete
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        reload
        """
        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

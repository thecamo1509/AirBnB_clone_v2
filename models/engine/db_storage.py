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
        """
        mylist = []
        objects = {}
        myclasses = {'cities': 'City', 'states': 'State', 'users': 'User',
                     'amenities': 'Amenity', 'places': 'Place',
                     'reviews': 'Review'}
        if cls:
            mylist = self.__session.query(eval(cls)).all()
        else:
            tables = self.__engine.table_names()
            for table in tables:
                mylist.append(self.__session.query(
                    eval(myclasses[table])).all())
        for obj in mylist:
            if type(obj) == list:
                for o in obj:
                    key = "{}.{}".format(o.__class__.__name__, o.id)
                    objects[key] = o
            else:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

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

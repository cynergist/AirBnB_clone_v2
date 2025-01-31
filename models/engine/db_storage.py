#!/usr/bin/python3
""" Database Storage Engine """

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel, Base
from os import getenv
import datetime


class DBStorage:
    """
    This class is the database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize an instance
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        query all objects from the current db session, based on class name
        """
        cls_result = {}
        cls_list = [State, City, User, Place, Review, Amenity]
        results = self.__session.query(eval(cls)).all()
        if cls:
            for cls_object in results:
                key = '{}.{}'.format(type(cls_object).__name__, cls_object.id)
                cls_result[key] = cls_object
        else:
                for classes in cls_list:
                    for cls_object in results:
                        key = '{}.{}'.format(type(cls_object).
                                             __name__, cls_object.id)
                        cls_result[key] = cls_object

        return cls_result

    def new(self, obj):
        """
        add the object to the current databse session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete obj from the current database session
        """
        if obj:
            self.__session.expunge(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """
        removes private session
        """
        self.__session.close()

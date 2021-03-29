#!/usr/bin/python3
"""Manages DBstorage Class"""
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy import (create_engine)
from models.amenity import Amenity
from models.base_model import Base
from models.review import Review
from models.state import State
from models.place import Place
from os import getenv as env
from models.user import User
from models.city import City


class DBStorage():
    """Class for logic of the DataBase"""
    __engine = None
    __session = None

    def __init__(self):
        """"""
        user = env("HBNB_MYSQL_USER")
        passwd = env("HBNB_MYSQL_PWD")
        host = env("HBNB_MYSQL_HOST")
        db = env("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""
        objDict = {}
        if cls:
            query = self.__session.query(eval(cls)).all()
            print(query)
            strKey = "{}.{}".format(cls, query.id)
            setattr(objDict, strKey, query)
        else:
            classList = ["State", "City"]
            for className in classList:
                obj = self.__session.query(eval(className)).all()
                print(obj)
                strKey = "{}.{}".format(className, obj.id)
                setattr(objDict, strKey, obj)
        return (objDict)

    def new(self, obj):
        """"""
        self.__session.add(obj)
        
    def save(self):
        """"""
        self.__session.commit()

    def delete(self, obj=None):
        """"""
        self.__session.delete(obj)

    def reload(self):
        """"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(expire_on_commit=False, bind=self.__engine)
        Session = scoped_session(session)
        self.__session = Session()

#!/usr/bin/python3
"""
DBStorage class is included.
"""

import models
from modelss.base_model import BaseModel, Base
from models.review import Review
from model.amenity import Amenity
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage:
    """Operates with the MYSQL database."""
    __engine = None
    __session = None

    def __init__(self):
        """Create an instance of the DBStorage class."""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))


        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Execute a query within the ongoing database session."""
        new_dict = {}
        for clss in classes.values():
            if cls is None or cls is clss:
                objs = self.__session.query(clss).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """Include the object in the ongoing database session."""
        self.__session.add(obj)

    def save(self):
        """Save all modifications made in the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Remove the object from the ongoing database session if it exists"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Retrieve data from the database again"""
        Base.metadata.create_all(self.__engine)
        sessionFactory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
        )
        self.__session = scoped_session(sessionFactory)()

    def close(self):
        """Invoke the remove() function on the private session attribute."""
        self.__session.remove()


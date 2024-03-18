#!/usr/bin/python3
"""
Module for user class

"""
import models
from models.base_model import BaseModel, Base
import os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, string

class User(BaseModel, Base):
    """
    User representation

    """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Creates a user instance.
        """
        super().__init__(*args, **kwargs)

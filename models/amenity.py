#!/usr/bin/python3
"""Define a class named Amenity."""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import sqlalchemy



class Amenity(BaseModel, Base):
    """The portrayal or depiction of an Amenity."""
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Creates an instance of the Amenity class."""
        super().__init__(*args, **kwargs)

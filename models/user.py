#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import orm
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

places = orm.relationship("Place", backref="user", cascade="all, delete-orphan")
reviews = orm.relationship("Review", backref="user", cascade="all, delete_orphan")


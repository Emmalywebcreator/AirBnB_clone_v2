#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state_id', cascade='all, delete-orphan')

    else:
        @property
        def cities(self):
            '''
                getter attribute cities that returns the list of City
                instances with state_id equals to the current State.id
            '''
            import models
            from models.city import City

            list_of_cities = models.storage.all('City').values()
            cities_by_state = [city for city in cities_by_state if city.state_id == self.id]
            return cities_by_state
#!/usr/bin/python3
""" Place Module for HBNB project """
from os import genv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
from models.review import Review
from models import storage


link_table = Table(
      "place_amenity", Base.metadata,
      Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
      Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False),
  )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('city_id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user_id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

reviews = relationship("Review", backref="place", cascade="all, delete_orphan")
amenities = relationship("Amenities", secondary="place_amenities", viewonly=False)


if ("HBNB_TYPE_STORAGE") != "db":
    @property
    def reviews(self):
        """Getter attribute reviews that returns the list of Review instances with place_id equals to the current Place.id"""

        all_reviews = storage.all(Review)
        return [review for review in all_reviews.values() if review.place_id == self.id]
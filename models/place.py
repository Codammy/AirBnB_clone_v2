#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id',
                             String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review',
                           backref='place', cascade='all, delete-orphan')
    amenities = relationship('Amenity',
                             secondary=place_amenity,
                             viewonly=False, backref='place_amenities')

    if os.getenv('HBNB_STORAGE_TYPE') == 'fs':
        @property
        def amenities(self):
            """
            returns the list of Amenity instances based on
            the attribute amenity_ids that contains all
            Amenity.id linked to the Place
            """
            from models.amenity import Amenity
            from models import storage
            all = storage.all(Amenity)
            return [inst for inst in all.values() if
                    inst['id'] in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """
            handles append method for adding an
            Amenity.id to the attribute amenity_ids
            """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

        @property
        def reviews(self):
            """
            returns the list of Review instances with place_id
            equals to the current Place.id
            """
            from models.review import Review
            from models import storage
            r = storage.all(Review)
            return [v for v in r.values() if c['id'] == self.id]

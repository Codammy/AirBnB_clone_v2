#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            from models import storage
            from models.city import City
            """
            that returns the list of City instances with
            state_id equals to the current State.id
            """
            c = storage.all(City)
            filtered_city = []
            for v in c.values():
                if v.state_id == self.id:
                    filtered_city.append(v)
            return filtered_city

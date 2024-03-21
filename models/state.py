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
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        from models import storage
        from models.city import City

        @property
        def cities(self):
            """
            that returns the list of City instances with
            state_id equals to the current State.id
            """
            c = storage.all(City)
            return [v for v in c.values() if c['id'] == self.id]

#!/usr/bin/python3
"""BDStorage Engine"""
import os
from sqlalchemy import (create_engine, MetaData)
from sqlalchemy.orm import (sessionmaker, scoped_session)
from models.base_model import (BaseModel, Base)
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.city import City
from models.review import Review


class DBStorage():
    __engine = None
    __session = None
    models = {"State": State,
              "Place": Place, "User": User, "City": City,
              "Amenity": Amenity, "Review": Review}

    def __init__(self):
        """initializes engine object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB'),
                                             ),
                                      pool_pre_ping=True
                                      )
        # self.__session = sessionmaker(bind=engine)
        if (os.getenv('HBNB_ENV') == 'test'):
            metadata = MetaData()
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all on the current database session"""
        objects = {}
        if not cls:
            for k, v in self.models.items():
                table = self.__session.query(v)
                objects.update({(k + row.id): row for row in table})
        else:
            classname = cls.__name__
            table = self.__session.query(cls)
            objects.update({(classname + '.' + row.id): row for row in table})
        return objects

    def new(self, obj):
        """adds obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj):
        """delete from current database session 'obj' if not none"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables is the database"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """ends the session"""
        self.__session.remove()

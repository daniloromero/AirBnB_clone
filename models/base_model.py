#!/usr/bin/python3
"""
BaseModel that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """Class definition"""
    def __init__(self, *args, **kwargs):
        """ Initialization on Base instance"""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if (key == "created_at" or key == "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation"""
        bsr = "[{:s}] ({:s}) {:s}"
        bsr = bsr.format(self.__class__.__name__, self.id, str(self.__dict__))
        return bsr

    def save(self):
        """updates public instance attr updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dclon = self.__dict__.copy()
        dclon["__class__"] = self.__class__.__name__
        dclon["created_at"] = self.created_at.isoformat()
        dclon["updated_at"] = self.updated_at.isoformat()
        return dclon

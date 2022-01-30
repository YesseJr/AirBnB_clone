#!/usr/bin/python3
"""
Defines the BaseModel class.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    Base class for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """
    
def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            
def __str__(self):
        """
        Return string of info about model
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))
        
def to_dict(self):
        """
        Return dic with string formats of times; add class info to dic
        """
        dictionary = {}
        dictionary["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        return dictionary                    

def save(self):
        """
        Update instance with updated time & save to serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()
        
def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())        

#!/usr/bin/python3
import uuid
from datetime import datetime
"""This module defines all common attributes.

The methods/attributes for other classes start here.
It defines a class ``BaseModel``
"""


class BaseModel:
    """A base model that has common attribute/methods for other classes.
    """

    def __init__(self):
        """Initializes the basemodel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of an object."""
        return f"{[self.__class__.__name__]} ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute update_at,
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__,
        of the instance.
        """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

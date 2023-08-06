#!/usr/bin/python3
""" base model super class """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Basmodel for other classes """

    def __init__(self, *args, **kwargs):
        """ initializes the class attributes*arg is an unused variable"""
        str_fdate = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at":
                    self.__dict__[k] = datetime.strptime(v, str_fdate)
                elif k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, str_fdate)
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """ string representation of the BaseModel intance """
        clName = self.__class__.__name__
        str = f"[{clName}] ({self.id}) {self.__dict__}"
        return str

    def save(self):
        """ updates the instance attribute update_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return all keys and values of the objectinstance from __dict__"""
        dictcopy = self.__dict__.copy()
        dictcopy["created_at"] = self.created_at.isoformat()
        dictcopy["updated_at"] = self.updated_at.isoformat()
        dictcopy["__class__"] = self.__class__.__name__
        return dictcopy

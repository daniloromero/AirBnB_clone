#!/usr/bin/python3
""" class that will inherit from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ this is the User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

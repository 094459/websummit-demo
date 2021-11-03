# config.py


import os


class BaseConfig(object):
     SECRET_KEY = 'hi'
     DEBUG = True
     DB_NAME = 'ricsue'
     DB_SERVICE = 'localhost'
     DB_PORT = 5432
     SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}/{2}'.format(
         DB_SERVICE, DB_PORT, DB_NAME
     )

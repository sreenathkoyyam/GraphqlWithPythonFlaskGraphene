#from datetime import datetime
from mongoengine import Document
from mongoengine.fields import ( StringField )
class Location(Document):

    meta = {'collection': 'Location'}
    name = StringField()
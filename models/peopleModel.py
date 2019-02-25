#from datetime import datetime
from mongoengine import Document
from mongoengine.fields import ( StringField )
class People(Document):

    meta = {'collection': 'People'}
    name = StringField()
    gender = StringField()
    created = StringField()
    edited = StringField()

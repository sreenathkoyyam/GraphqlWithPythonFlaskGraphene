from datetime import datetime
from mongoengine import EmbeddedDocument
from mongoengine.fields import ( EmbeddedDocumentField, DateTimeField, StringField)

class Task(EmbeddedDocument):

    name = StringField()
    deadline = DateTimeField(default=datetime.now)


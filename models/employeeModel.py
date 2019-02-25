from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, EmbeddedDocumentField,
    ListField, ReferenceField, StringField,
)
from .locationModel import Location
from .rolesModel import Role
from .departmentModel import Department
from .taskModel import Task

class Employee(Document):

    meta = {'collection': 'employee'}
    name = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(Department)
    locations = ListField(ReferenceField(Location))
    roles = ListField(ReferenceField(Role))
    leader = ReferenceField('Employee')
    tasks = ListField(EmbeddedDocumentField(Task))

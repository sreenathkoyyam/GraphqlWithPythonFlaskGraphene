from graphene_mongo import  MongoengineObjectType

from models.taskModel import Task as TaskModel
from graphene.relay import Node


class Task(MongoengineObjectType):

    class Meta:
        model = TaskModel
        interfaces = (Node,)
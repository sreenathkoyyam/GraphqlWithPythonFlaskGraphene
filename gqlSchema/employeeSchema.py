from graphene_mongo import  MongoengineObjectType
from models.employeeModel import Employee as EmployeeModel
from graphene.relay import Node


class Employee(MongoengineObjectType):

    class Meta:
        model = EmployeeModel
        interfaces = (Node,)

from graphene_mongo import  MongoengineObjectType
from resolvers.departmentModel import Department as DepartmentModel
from graphene.relay import Node

class Department(MongoengineObjectType):

    class Meta:
        model = DepartmentModel
        interfaces = (Node,)

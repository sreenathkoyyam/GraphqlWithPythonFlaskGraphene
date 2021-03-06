from graphene_mongo import  MongoengineObjectType

from models.rolesModel import Role as RoleModel
from graphene.relay import Node

class Role(MongoengineObjectType):

    class Meta:
        model = RoleModel
        interfaces = (Node,)
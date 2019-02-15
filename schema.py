import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from gqlSchema.employeeSchema import Employee
from gqlSchema.departmentSchema import Department
from gqlSchema.roleSchema import Role
from gqlSchema.locationSchema import Location
from gqlSchema.taskSchema import Task






class Query(graphene.ObjectType):
    node = Node.Field()
    all_employees = MongoengineConnectionField(Employee)
    all_roles = MongoengineConnectionField(Role)
    role = graphene.Field(Role)

schema = graphene.Schema(query=Query, types=[Department, Employee, Role,Location])


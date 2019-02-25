import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from gqlSchema.employeeSchema import Employee
from gqlSchema.departmentSchema import Department
from gqlSchema.roleSchema import Role
from gqlSchema.locationSchema import Location
from gqlSchema.schema_people import People,CreatePerson
from gqlSchema.taskSchema import Task






class Query(graphene.ObjectType):
    node = Node.Field()
    all_employees = MongoengineConnectionField(Employee)
    all_roles = MongoengineConnectionField(Role)
    role = graphene.Field(Role)
    all_locations = MongoengineConnectionField(Location)
    # People
    people = graphene.relay.Node.Field(People)
    all_people = MongoengineConnectionField(People)


class Mutation(graphene.ObjectType):
        """Mutations which can be performed by this API."""
        # Person mutation
        createPerson = CreatePerson.Field()
        #updatePerson = schema_people.UpdatePerson.Field()




schema = graphene.Schema(query=Query, mutation=Mutation, types=[Department, Employee, Role,Location])


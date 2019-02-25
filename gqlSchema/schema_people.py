''' from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.base import db_session
from database.model_people import ModelPeople
import graphene
import utils '''
import graphene
from graphene_mongo import  MongoengineObjectType
from models.peopleModel import People as PeopleModel
from graphene.relay import Node
from connector.mongo.base import db
from controllers.peopleController import PeopleController
import json
from flask import jsonify
from models.utils import utils
from datetime import datetime

PeopleController = PeopleController()
# Create a generic class to mutualize description of people attributes for both queries and mutations
class PeopleAttribute:
    name = graphene.String(description="Name of the person.")
    gender = graphene.String(description="Gender of the person.")
   # emp_id = graphene.ID(description="Global Id of the planet from which the person comes from.")


class People(MongoengineObjectType):
    """People node."""

    class Meta:
        model = PeopleModel
        interfaces = (Node,)
        #interfaces = (graphene.relay.Node,)


class CreatePersonInput(graphene.InputObjectType, PeopleAttribute):
    """Arguments to create a person."""
    pass


class CreatePerson(graphene.Mutation):
    """Mutation to create a person."""
    person = graphene.Field(lambda: People, description="Person created by this mutation.")
    class Arguments:
        input = CreatePersonInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        #data['created'] = datetime.utcnow()
        #data['edited'] = datetime.utcnow()

        PeopleController.insertData(data)
        data['id']= data.pop('_id')
        #data={'id': '5c6d165715091d4bb8fee4cf', 'name': 'Sree', 'gender': 'M'}
        person = PeopleModel(**data)
        return CreatePerson(person=person)



    '''def mutate(self, info, input):
        print('hiiiisdse')
       data = utils.input_to_dictionary()
        print('hiiiise')
        print(data)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()
       # result = list(db.db.People.find({"name": "sree"}))
        #data = PeopleController.get_people_data()
        person1 = PeopleModel(**data)

        person = {"data": {
        "createPerson": {
        "person": data
        }
        }
        }
        #person = json.dumps(person)
       # person = PeopleModel(name="card", gender= "F")
       # person.save()
       # db_session.add(person)
        #db_session.commit()

        return CreatePerson(person=person1)'''


'''class UpdatePersonInput(graphene.InputObjectType, PeopleAttribute):
    """Arguments to update a person."""
    id = graphene.ID(required=True, description="Global Id of the person.")


class UpdatePerson(graphene.Mutation):
    """Update a person."""
    person = graphene.Field(lambda: People, description="Person updated by this mutation.")

    class Arguments:
        input = UpdatePersonInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        person = db_session.query(ModelPeople).filter_by(id=data['id'])
        person.update(data)
        db_session.commit()
        person = db_session.query(ModelPeople).filter_by(id=data['id']).first()

        return UpdatePerson(person=person) '''

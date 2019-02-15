from mongoengine import connect

from models import Department, Employee, Task
from resolvers.locationModel import Location
from resolvers.rolesModel import Role
connect('graphene-mongo-example', host='mongodb://127.0.0.1:27017', alias='default')


def init_db():
    # Create the fixtures
    engineering = Department(name='Engineering')
    engineering.save()

    hr = Department(name='Human Resources')
    hr.save()

    manager = Role(name='manager')
    manager.save()
    koyyam = Location(name='koyyam')
    koyyam.save()
    #Kannur = Location(name='Koyyam')
    #Kannur.save()
    engineer = Role(name='engineer')
    engineer.save()

    debug = Task(name='Debug')
    test = Task(name='Test')

    tracy = Employee(
        name='Tracy',
        department=hr,
        roles=[engineer, manager],
        tasks=[]
    )
    tracy.save()

    peter = Employee(
        name='Peter',
        department=engineering,
        leader=tracy,
        locations=[koyyam],
        roles=[engineer],
        tasks=[debug, test]
    )
    peter.save()

    roy = Employee(
        name='Roy',
        department=engineering,
        leader=tracy,
       # location=[Kannur],
        roles=[engineer],
        tasks=[debug]
    )
    roy.save()

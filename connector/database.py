from mongoengine import connect

from models.departmentModel import Department
from models.employeeModel import Employee
from models.taskModel import Task
from models.locationModel import Location
from models.rolesModel import Role
from models.peopleModel import People
connect('graphene-mongo', host='mongodb://127.0.0.1:27017', alias='default')


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
    sree = People(name='Sree',gender="M")
    sree.save()
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

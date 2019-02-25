import requests
import responses
from connector.mongo.base import db

class PeopleController(object):



    '''
    #To list all the documents in the collection
    :param self:
    :return: returns data from mongodb
    '''

    def get_people_data(self):

        try:

            result = list(db.db.People.find({}))
            print(result)
        except:
            result = []
        data=[]
        for each_result in result:
            item={"name":"sss","gender":"M"}
            data.append(item);
        print('hjkk', data)
        return data

    def insertData(self,data):


        try:
            result = list(db.db.People.insert(data))
        except:
            result = []

        return result


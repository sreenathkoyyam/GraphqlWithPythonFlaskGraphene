from connector.database import init_db
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from connector.mongo.base import db

app = Flask(__name__)
app.debug = True
app.config['MONGO_URI']= "mongodb://127.0.0.1:27017/graphene-mongo"

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    # for inserting dummy data to mongodb collection
    init_db()
    db.init_app(app)
    app.run()



default_query = '''
{
  allEmployees {
    edges {
      node {
        id,
        name,
        department {
          id,
          name
        },
        roles {
          edges {
            node {
              id,
              name
            }
          }
        },
        leader {
          id,
          name
        }
        tasks {
          edges {
            node {
              name,
              deadline
            }
          }
        }
      }
    }
  }
}'''.strip()
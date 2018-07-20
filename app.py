#CRUD API's create, read, update,  delete
# run from terminal only using "python coded\app.py" as the data.db file is in another folder as giver an error.

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.items import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # configuration property
app.secret_key =  "tejas"  # The secret key is used to encrypt the JWT. That is how we encrypt the user info into a secured token
api = Api(app)

jwt = JWT(app, authenticate, identity)                         # JWT creates a new endpoint '/auth'

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')  # http://127.0.0.1:5000/student/Tejas
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__ == "__main__":                       # to prevent the flask app from running if we were to import something from app.py
    # main is the name assigned when we run a file, so if we do not run a file then no name is assigned and this condition is false
    from db import db
    db.init_app(app)      # links together your Flask app with SQLAlchemy
    app.run(port=5000, debug = True)

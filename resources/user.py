import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):  # it is a resource so we can add it to API using flask_restful and also we only need to use 'post'
    parser = reqparse.RequestParser()  # obeject to parse the request
    parser.add_argument("username",
                        type=str,  # to deal with float type price
                        required=True,  # no request without price can come through
                        help="This field cannot be left blank"
                        )
    parser.add_argument("password",
                        type=str,  # to deal with float type price
                        required=True,  # no request without price can come through
                        help="This field cannot be left blank"
                        )


    def post(self):   # this gets called when we post some data to the UserRegister
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]) is not None:
            return {"message": "Username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "user created successfully."}, 201   # 201 - created


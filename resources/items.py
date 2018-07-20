from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):                                          # inheritence
    parser = reqparse.RequestParser()  # obeject to parse the request
    parser.add_argument("price",
                        type=float,  # to deal with float type price
                        required=True,  # no request without price can come through
                        help="This field cannot be left blank"
                        )
    parser.add_argument("store_id",
                        type=int,  # to deal with float type price
                        required=True,  # no request without price can come through
                        help="Every item needs a store id"
                        )


    @jwt_required()                                            # authorization check karne k liye
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()         # as ItemModel returns a object and not a dictionary
        return {"message": "item not founddd"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "an item with name {} already exists".format(name)}, 400

        data = Item.parser.parse_args()      # gonna parse the arguments that come through the json payload and going to put the valid ones in data

        item = ItemModel(name, **data)        #data["price"], data["store_id"]        # ItemModel object

        try:
            item.save_to_db()
        except:
            return {"message": "An error occured while inserting the item"}, 500  # internal server error

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": "item {} deleted".format(name)}

    def put(self,name):                                         # we can update or create items
        data = Item.parser.parse_args()              # gonna parse the arguments that come through the json payload and going to put the valid ones in data
        print(data)

        item = ItemModel.find_by_name(name)     # from database

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data["price"]

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]} #list comprehension
       # return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}    # lambda function


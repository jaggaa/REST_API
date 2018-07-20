from db import db

class ItemModel(db.Model):   # internal representation so it also contains property of an item as object property
    __tablename__ = "items"  # the table name items

    # column name same as in init method
    id = db.Column(db.Integer, primary_key=True)  # id column
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precesion=2))

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))    #to create a link between item and store (diag copy me)
    store = db.relationship("StoreModel")   # to find the store in the database with the store id

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):   #return the json represeentation of the model
        return {"name": self.name, "price": self.price}  # dictionary representing our item

    @classmethod     # beacause it's gonna return an object of ItemModel and nota dictionary
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()   #select * from items where name= name limit=1

    def save_to_db(self):      # does both inserting and updating
        db.session.add(self)    # collection of objects we write to the database
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

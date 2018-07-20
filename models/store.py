from db import db

class StoreModel(db.Model):   # internal representation so it also contains property of an item as object property
    __tablename__ = "stores"  # the table name items

    # column name same as in init method
    id = db.Column(db.Integer, primary_key=True)  # id column
    name = db.Column(db.String(80))

    items = db.relationship("ItemModel", lazy = "dynamic")     # allows store to see which items are in the database with same store id

    def __init__(self, name):
        self.name = name

    def json(self):   #return the json represeentation of the model
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}  # dictionary representing our item

    @classmethod     # beacause it's gonna return an object of ItemModel and nota dictionary
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()   #select * from items where name= name limit=1

    def save_to_db(self):      # does both inserting and updating
        db.session.add(self)    # collection of objects we write to the database
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

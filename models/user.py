from db import db


class UserModel(db.Model):
    __tablename__ = "users"   # the table name users

    # column name same as in init method
    id = db.Column(db.Integer, primary_key = True)  # id column
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):      # does both inserting and updating
        db.session.add(self)    # collection of objects we write to the database
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):   # find the user in the database by the users username
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):   # find the user in the database by the users _id
        return cls.query.filter_by(id = _id).first()
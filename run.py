from db import db
from app import app

db.init_app(app)

@app.before_first_request      # runs the method below it before the first request into this app
def create_tables():
    db.create_all()
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Contact
from flask_cors import CORS
from flask_migrate import Migrate

BASEDIR = os.path.abspath(os.path.dirname(__file__))
app = Flask (__name__)
db.init_app(app)
CORS(app)
Migrate (app, db)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BASEDIR, "test.db") #Dirección provisoria de la base de datos
app.config['DEBUG'] = True


@app.route ('/contact', methods=['POST'])
def new_contact():
    contact = Contact()
    contact.full_name = request.json.get("full_name")
    contact.email = request.json.get("email")
    contact.address = request.json.get("address")
    contact.phone = request.json.get("phone")

    db.session.add(contact)
    db.session.commit()
    return jsonify(contact.serialize()), 200




if __name__ == '__main__':
    app.run(host='localhost', port=8000)
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root@localhost/ids")

def registrar(name, name_pet, email, contact, city):
    conn = engine.connect()
    query = """INSERT INTO pets (name, name_pet, email, contact, city) VALUES (:name, :name_pet, :email, :contact, :city);"""
    try:
        result = conn.execute(text(query), name=name, name_pet=name_pet, email=email, contact=contact, city=city)
        #Una vez ejecutada la consulta, se debe hacer commit de la misma para que
        #se aplique en la base de datos.
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error' + str(err.__cause__)})


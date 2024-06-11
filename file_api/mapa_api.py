from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root:12345@localhost/lost_pets_db")

def obtener_coordenadas():
    conn = engine.connect()
    query = "SELECT latitud, altitud FROM coordenadas;"
    try:
        result = conn.execute(text(query))
        conn.close()
    except Exception as e:
        return jsonify({'message': 'Se ha producido un error: ' + str(e)}), 500

    data = [{'latitud': row[0], 'altitud': row[1]} for row in result]

    return jsonify(data), 200
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root:12345@localhost/lost_pets_db")


@app.route('/informantes', methods=['GET'])
def get_informants():
    conn = engine.connect()
    query = "SELECT * FROM informante;"
    try:
        result = conn.execute(text(query))
        data = []
        for row in result:
            entity = {
                'id_informante': row.id_informante,
                'nombre': row.nombre,
                'telefono': row.telefono,
                'barrio': row.barrio
            }
            data.append(entity)
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify(data), 200

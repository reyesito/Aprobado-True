from flask import jsonify
from sqlalchemy import text, create_engine
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root:12345@localhost:3308/lost_pets_db")

#Funcion de Mapa de coordenadas
def obtener_coordenadas():
    conn = engine.connect()
    query = "SELECT latitud, altitud FROM coordenadas;"
    try:
        result = conn.execute(text(query))
        conn.close()
    except Exception as e:
        return None, 500

    data = [{'latitud': row[0], 'altitud': row[1]} for row in result]

    return data, 200
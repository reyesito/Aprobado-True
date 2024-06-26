from flask import jsonify
from sqlalchemy import text, create_engine
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root:12345@localhost:3308/lost_pets_db")
def obtener_coordenadas():
    conn = engine.connect()
    query = """
        SELECT latitud, altitud, 'refugio' AS tipo, nombre AS info FROM coordenadas
        UNION
        SELECT latitud, altitud, 'mascota_encontrada' AS tipo, id_mascota AS info FROM mascotas_encontradas
        UNION
        SELECT latitud, altitud, 'mascota_perdida' AS tipo, id_mascota AS info FROM mascotas_perdidas
    """
    try:
        result = conn.execute(text(query))
        data = [{'latitud': row[0], 'altitud': row[1], 'tipo': row[2], 'info': row[3]} for row in result]
        conn.close()
        return data, 200
    except Exception as e:
        return None, 500


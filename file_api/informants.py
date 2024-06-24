from flask import jsonify
from sqlalchemy import text, create_engine
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root:12345@localhost:3308/lost_pets_db")

def crear_informante(data_informant):
    conn = engine.connect()
    query = f"""INSERT INTO informantes (nombre, mail, telefono, barrio) 
                VALUES ('{data_informant["user_name"]}', '{data_informant["mail"]}', {data_informant["telephone"]}, '{data_informant["city"]}');"""
    try:
        result = conn.execute(text(query))
        conn.commit()
        informante_id = result.lastrowid #aca obtengo el id
        conn.close()
        return informante_id
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

def obtener_informantes():
    conn = engine.connect()
    query = "SELECT * FROM informantes;"
    try:
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500

    data = []
    for row in result:
        entity = {
            'id_informante': row.id_informante,
            'nombre': row.nombre,
            'mail': row.mail,
            'telefono': row.telefono,
            'barrio': row.barrio
        }
        data.append(entity)

    return jsonify(data), 200

def obtener_informante(id_informant):
    conn = engine.connect()
    query = f"SELECT * FROM informantes WHERE id_informante = {id_informant};"
    try:
        result = conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    if result.rowcount != 0:
        row = result.first()
        data = {
            'id_informante': row.id_informante,
            'nombre': row.nombre,
            'mail': row.mail,
            'telefono': row.telefono,
            'barrio': row.barrio
        }
        return jsonify(data), 200
    return jsonify({"message": "El informante no existe"}), 404

def borrar_informante(id_informant):
    conn = engine.connect()
    query = f"DELETE FROM informantes WHERE id_informante = {id_informant};"
    validation_query = f"SELECT * FROM informantes WHERE id_informante = {id_informant};"
    try:
        val_result = conn.execute(text(validation_query))
        if val_result.rowcount != 0:
            conn.execute(text(query))
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({"message": "El informante no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    return jsonify({'message': 'Se ha eliminado correctamente'}), 202

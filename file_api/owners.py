from flask import jsonify
from sqlalchemy import text, create_engine
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root:12345@localhost:3308/lost_pets_db")

def crear_duenio(data_owner):
    conn = engine.connect()
    query = f"""INSERT INTO duenios (nombre, mail, telefono, barrio) 
                VALUES ('{data_owner["user_name"]}', '{data_owner["mail"]}', '{data_owner["telephone"]}', '{data_owner["city"]}');"""
    try:
        result = conn.execute(text(query))
        conn.commit()
        duenio_id = result.lastrowid #aca obtengo el id
        conn.close()
        return duenio_id
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500


def obtener_duenios():
    conn = engine.connect()
    query = "SELECT * FROM duenios;"
    try:
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500

    data = []
    for row in result:
        entity = {
            'id_duenio': row.id_duenio,
            'nombre': row.nombre,
            'mail': row.mail,
            'telefono': row.telefono,
            'barrio': row.barrio
        }
        data.append(entity)

    return jsonify(data), 200

def obtener_duenio(id_owner):
    conn = engine.connect()
    query = f"SELECT * FROM duenios WHERE id_duenio = {id_owner};"
    try:
        result = conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    if result.rowcount != 0:
        row = result.first()
        data = {
            'id_duenio': row.id_duenio,
            'nombre': row.nombre,
            'mail': row.mail,
            'telefono': row.telefono,
            'barrio': row.barrio
        }
        return jsonify(data), 200
    return jsonify({"message": "El dueño no existe"}), 404

def borrar_duenio(id_owner):
    conn = engine.connect()
    query = f"DELETE FROM duenios WHERE id_duenio = {id_owner};"
    validation_query = f"SELECT * FROM duenios WHERE id_duenio = {id_owner};"
    try:
        val_result = conn.execute(text(validation_query))
        if val_result.rowcount != 0:
            conn.execute(text(query))
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({"message": "El dueño no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    return jsonify({'message': 'Se ha eliminado correctamente'}), 202

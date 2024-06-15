from flask import jsonify
from sqlalchemy import text, create_engine
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root:12345@localhost:3308/lost_pets_db")

def crear_mascota_encontrada(data_pet):
    conn = engine.connect()
    query = f"""INSERT INTO mascotas_encontradas (animal, raza, nombre, color, sexo, tamanio, mail_informante, telefono_informante, latitud, altitud)
                VALUES ('{data_pet["animal"]}', '{data_pet["type_class"]}', '{data_pet["pet_name"]}', '{data_pet["color"]}', '{data_pet["sex"]}', '{data_pet["size"]}', '{data_pet["mail"]}', '{data_pet["telephone"]}', '{data_pet["latitude"]}', '{data_pet["longitude"]}');"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500


def obtener_mascotas_encontradas():
    conn = engine.connect()
    query = "SELECT * FROM mascotas_encontradas;"
    try:
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500

    data = []
    for row in result:
        entity = {
            'id_mascota': row.id_mascota,
            'animal':row.animal,
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'tamanio': row.tamanio,
            'mail_informante': row.mail_informante,
            'telefono_informante': row.telefono_informante,
            'id_informante' : row.id_informante
        }
        data.append(entity)
    conn.close() 
    return data  

def obtener_mascota_encontrada(id_mascota):
    conn = engine.connect()
    query = f"SELECT * FROM mascotas_encontradas WHERE id_mascota = {id_mascota};"
    try:
        result = conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    if result.rowcount != 0:
        row = result.first()
        data = {
            'id_mascota': row.id_mascota,
            'animal':row.animal,
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'tamanio': row.tamanio,
            'mail_informante': row.mail_informante,
            'telefono_informante': row.telefono_informante,
            'id_informante' :row.id_informante,
        }
        return jsonify(data), 200
    return jsonify({"message": "La mascota no existe"}), 404

def borrar_mascota_encontrada(id_pet):
    conn = engine.connect()
    query = f"DELETE FROM mascotas_encontradas WHERE id_mascota = {id_pet};"
    validation_query = f"SELECT * FROM mascotas_encontradas WHERE id_mascota = {id_pet};"
    try:
        val_result = conn.execute(text(validation_query))
        if val_result.rowcount != 0:
            conn.execute(text(query))
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({"message": "La mascota no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    return jsonify({'message': 'Se ha eliminado correctamente'}), 202

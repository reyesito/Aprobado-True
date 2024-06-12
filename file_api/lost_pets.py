from flask import jsonify
from sqlalchemy import text, create_engine
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root:12345@localhost:3308/lost_pets_db")

def crear_mascota_perdida(data_lost_pet):
    conn = engine.connect()
    query = f"""INSERT INTO mascotas_perdidas (animal,raza, nombre, color, sexo, edad_aprox, tamanio, barrio, mail_duenio, telefono_duenio) 
                VALUES ('{data_lost_pet["animal"]}','{data_lost_pet["type_class"]}', '{data_lost_pet["pet_name"]}', '{data_lost_pet["color"]}', '{data_lost_pet["sex"]}',
                        '{data_lost_pet["size"]}', '{data_lost_pet["city"]}',
                        '{data_lost_pet["mail"]}', '{data_lost_pet["telephone"]}');"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201

def obtener_mascotas_perdidas():
    conn = engine.connect()
    query = "SELECT * FROM mascotas_perdidas;"
    try:
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500

    data = []
    for row in result:
        entity = {
            'id_mascota': row.id_mascota,
            'animal': row.animal,
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'tamanio': row.tamanio,
            'barrio': row.barrio,
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio,
            'id_duenio': row.id_duenio
        }
        data.append(entity)

    return jsonify(data), 200

def obtener_mascota_perdida(id_lost_pet):
    conn = engine.connect()
    query = f"SELECT * FROM mascotas_perdidas WHERE id_mascota = {id_lost_pet};"
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
            'animal': row.animal,
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'tamanio': row.tamanio,
            'barrio': row.barrio,
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio,
            'id_duenio': row.id_duenio
        }
        return jsonify(data), 200
    return jsonify({"message": "La mascota no existe"}), 404

def borrar_mascota_perdida(id_lost_pet):
    conn = engine.connect()
    query = f"DELETE FROM mascotas_perdidas WHERE id_mascota = {id_lost_pet};"
    validation_query = f"SELECT * FROM mascotas_perdidas WHERE id_mascota = {id_lost_pet};"
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
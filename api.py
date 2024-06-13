from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root:12345@localhost:3308/lost_pets_db")

#Funcionalidades de crear:
def crear_duenio(data_owner):
    conn = engine.connect()
    query = f"""INSERT INTO duenios (nombre, mail, telefono, barrio) 
                VALUES ('{data_owner["user_name"]}', '{data_owner["mail"]}', '{data_owner["telephone"]}', '{data_owner["city"]}');"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201

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

def crear_informante(data_informant):
    conn = engine.connect()
    query = f"""INSERT INTO informantes (nombre,mail, telefono, barrio) 
                VALUES ('{data_informant["user_name"]}','{data_informant["mail"]}', {data_informant["telephone"]}, '{data_informant["city"]}');"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201

def crear_mascota_encontrada(data_pet):
    conn = engine.connect()
    query = f"""INSERT INTO mascotas_encontradas (animal,raza, nombre, color, sexo, tamanio, barrio, mail_informante, telefono_informante) 
                VALUES ('{data_pet["animal"]}','{data_pet["type_class"]}', '{data_pet["pet_name"]}', '{data_pet["color"]}', '{data_pet["sex"]}',
                        '{data_pet["size"]}', '{data_pet["city"]}',
                        '{data_pet["mail"]}', '{data_pet["telephone"]}');"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201


#Funcionalidades de obtener:

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
            'animal':row.animal,
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'tamanio': row.tamanio,
            'barrio': row.barrio,
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio,
            'id_duenio' : row.id_duenio
        }
        data.append(entity)
    conn.close() 
    return data  

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
            'barrio': row.barrio,
            'mail_informante': row.mail_informante,
            'telefono_informante': row.telefono_informante,
            'id_informante' : row.id_informante
        }
        data.append(entity)
    conn.close() 
    return data  

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
            'animal':row.animal,
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'tamanio': row.tamanio,
            'barrio': row.barrio,
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio,
            'id_duenio' : row.id_duenio
        }
        return jsonify(data), 200
    return jsonify({"message": "La mascota no existe"}), 404

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
            'mail' : row.mail,
            'telefono': row.telefono,
            'barrio': row.barrio
        }
        return jsonify(data), 200
    return jsonify({"message": "El informante no existe"}), 404

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
            'barrio': row.barrio,
            'mail_informante': row.mail_informante,
            'telefono_informante': row.telefono_informante,
            'id_informante' :row.id_informante,
        }
        return jsonify(data), 200
    return jsonify({"message": "La mascota no existe"}), 404

#Funcionalidades de borrar:

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




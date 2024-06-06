from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root@localhost/ids")

#Funcionalidades de duenios:

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

def crear_duenio():
    conn = engine.connect()
    new_duenio = request.get_json()
    query = f"""INSERT INTO duenios (nombre, mail, telefono, barrio) 
                VALUES ('{new_duenio["nombre"]}', '{new_duenio["mail"]}', {new_duenio["telefono"]}, '{new_duenio["barrio"]}');"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201

def actualizar_duenio(id_duenio):
    conn = engine.connect()
    mod_duenio = request.get_json()
    query = f"""UPDATE duenios SET nombre = '{mod_duenio['nombre']}'
                {f", mail = '{mod_duenio['mail']}'" if "mail" in mod_duenio else ""}
                {f", telefono = {mod_duenio['telefono']}" if "telefono" in mod_duenio else ""}
                {f", barrio = '{mod_duenio['barrio']}'" if "barrio" in mod_duenio else ""}
                WHERE id_duenio = {id_duenio};"""
    query_validation = f"SELECT * FROM duenios WHERE id_duenio = {id_duenio};"
    try:
        val_result = conn.execute(text(query_validation))
        if val_result.rowcount != 0:
            conn.execute(text(query))
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({'message': "El dueño no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify({'message': str(err.__cause__)}), 500
    return jsonify({'message': 'Se ha modificado correctamente'}), 200

def obtener_duenio(id_duenio):
    conn = engine.connect()
    query = f"SELECT * FROM duenios WHERE id_duenio = {id_duenio};"
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

def borrar_duenio(id_duenio):
    conn = engine.connect()
    query = f"DELETE FROM duenios WHERE id_duenio = {id_duenio};"
    validation_query = f"SELECT * FROM duenios WHERE id_duenio = {id_duenio};"
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

#Funcionalidades de Informantes

def obtener_informantes():
    conn = engine.connect()
    query = "SELECT * FROM informante;"
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
            'telefono': row.telefono,
            'barrio': row.barrio
        }
        data.append(entity)

    return jsonify(data), 200

def crear_informante():
    conn = engine.connect()
    new_informante = request.get_json()
    query = f"""INSERT INTO informante (nombre, telefono, barrio) 
                VALUES ('{new_informante["nombre"]}', {new_informante["telefono"]}, '{new_informante["barrio"]}');"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201

def actualizar_informante(id_informante):
    conn = engine.connect()
    mod_informante = request.get_json()
    query = f"""UPDATE informante SET nombre = '{mod_informante['nombre']}'
                {f", telefono = {mod_informante['telefono']}" if "telefono" in mod_informante else ""}
                {f", barrio = '{mod_informante['barrio']}'" if "barrio" in mod_informante else ""}
                WHERE id_informante = {id_informante};"""
    query_validation = f"SELECT * FROM informante WHERE id_informante = {id_informante};"
    try:
        val_result = conn.execute(text(query_validation))
        if val_result.rowcount != 0:
            conn.execute(text(query))
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({'message': "El informante no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify({'message': str(err.__cause__)}), 500
    return jsonify({'message': 'Se ha modificado correctamente'}), 200

def obtener_informante(id_informante):
    conn = engine.connect()
    query = f"SELECT * FROM informante WHERE id_informante = {id_informante};"
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
            'telefono': row.telefono,
            'barrio': row.barrio
        }
        return jsonify(data), 200
    return jsonify({"message": "El informante no existe"}), 404

def borrar_informante(id_informante):
    conn = engine.connect()
    query = f"DELETE FROM informante WHERE id_informante = {id_informante};"
    validation_query = f"SELECT * FROM informante WHERE id_informante = {id_informante};"
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

#Funcionalidades de Mascotas perdidas

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
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'edad_aprox': row.edad_aprox,
            'tamanio': row.tamanio,
            'barrio': row.barrio,
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio
        }
        data.append(entity)

    return jsonify(data), 200

def crear_mascota_perdida():
    conn = engine.connect()
    new_mascota = request.get_json()
    query = f"""INSERT INTO mascotas_perdidas (raza, nombre, color, sexo, edad_aprox, tamanio, barrio, mail_duenio, telefono_duenio) 
                VALUES ('{new_mascota["raza"]}', '{new_mascota["nombre"]}', '{new_mascota["color"]}', '{new_mascota["sexo"]}',
                        '{new_mascota["edad_aprox"]}', '{new_mascota["tamanio"]}', '{new_mascota["barrio"]}',
                        '{new_mascota["mail_duenio"]}', {new_mascota["telefono_duenio"]});"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201

def actualizar_mascota_perdida(id_mascota):
    conn = engine.connect()
    mod_mascota = request.get_json()
    query = f"""UPDATE mascotas_perdidas SET raza = '{mod_mascota['raza']}', nombre = '{mod_mascota['nombre']}',
                color = '{mod_mascota['color']}', sexo = '{mod_mascota['sexo']}', edad_aprox = '{mod_mascota['edad_aprox']}',
                tamanio = '{mod_mascota['tamanio']}', barrio = '{mod_mascota['barrio']}', 
                mail_duenio = '{mod_mascota['mail_duenio']}', telefono_duenio = {mod_mascota['telefono_duenio']}
                WHERE id_mascota = {id_mascota};"""
    query_validation = f"SELECT * FROM mascotas_perdidas WHERE id_mascota = {id_mascota};"
    try:
        val_result = conn.execute(text(query_validation))
        if val_result.rowcount != 0:
            conn.execute(text(query))
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({'message': "La mascota no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify({'message': str(err.__cause__)}), 500
    return jsonify({'message': 'Se ha modificado correctamente'}), 200

def obtener_mascota_perdida(id_mascota):
    conn = engine.connect()
    query = f"SELECT * FROM mascotas_perdidas WHERE id_mascota = {id_mascota};"
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
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'edad_aprox': row.edad_aprox,
            'tamanio': row.tamanio,
            'barrio': row.barrio,
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio
        }
        return jsonify(data), 200
    return jsonify({"message": "La mascota no existe"}), 404

def borrar_mascota_perdida(id_mascota):
    conn = engine.connect()
    query = f"DELETE FROM mascotas_perdidas WHERE id_mascota = {id_mascota};"
    validation_query = f"SELECT * FROM mascotas_perdidas WHERE id_mascota = {id_mascota};"
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

#FUncinoalidades de mascotas encontradas

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
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'tamanio': row.tamanio,
            'edad_aprox': row.edad_aprox,
            'barrio': row.barrio,
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio,
            'telefono_informante': row.telefono_informante,
            'id_informante': row.id_informante
        }
        data.append(entity)

    return jsonify(data), 200

def crear_mascota_encontrada():
    conn = engine.connect()
    new_mascota = request.get_json()
    query = f"""INSERT INTO mascotas_encontradas (raza, nombre, color, sexo, tamanio, edad_aprox, barrio,
                mail_duenio, telefono_duenio, telefono_informante, id_informante) 
                VALUES ('{new_mascota["raza"]}', '{new_mascota["nombre"]}', '{new_mascota["color"]}', 
                '{new_mascota["sexo"]}', '{new_mascota["tamanio"]}', '{new_mascota["edad_aprox"]}', 
                '{new_mascota["barrio"]}', '{new_mascota["mail_duenio"]}', {new_mascota["telefono_duenio"]},
                {new_mascota["telefono_informante"]}, {new_mascota["id_informante"]});"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201

def actualizar_mascota_encontrada(id_mascota):
    conn = engine.connect()
    mod_mascota = request.get_json()
    query = f"""UPDATE mascotas_encontradas SET raza = '{mod_mascota['raza']}', nombre = '{mod_mascota['nombre']}',
                color = '{mod_mascota['color']}', sexo = '{mod_mascota['sexo']}', tamanio = '{mod_mascota['tamanio']}',
                edad_aprox = '{mod_mascota['edad_aprox']}', barrio = '{mod_mascota['barrio']}',
                mail_duenio = '{mod_mascota['mail_duenio']}', telefono_duenio = {mod_mascota['telefono_duenio']},
                telefono_informante = {mod_mascota['telefono_informante']}, id_informante = {mod_mascota['id_informante']}
                WHERE id_mascota = {id_mascota};"""
    query_validation = f"SELECT * FROM mascotas_encontradas WHERE id_mascota = {id_mascota};"
    try:
        val_result = conn.execute(text(query_validation))
        if val_result.rowcount != 0:
            conn.execute(text(query))
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({'message': "La mascota no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify({'message': str(err.__cause__)}), 500
    return jsonify({'message': 'Se ha modificado correctamente'}), 200

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
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'tamanio': row.tamanio,
            'edad_aprox': row.edad_aprox,
            'barrio': row.barrio,
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio,
            'telefono_informante': row.telefono_informante,
            'id_informante': row.id_informante
        }
        return jsonify(data), 200
    return jsonify({"message": "La mascota no existe"}), 404

def borrar_mascota_encontrada(id_mascota):
    conn = engine.connect()
    query = f"DELETE FROM mascotas_encontradas WHERE id_mascota = {id_mascota};"
    validation_query = f"SELECT * FROM mascotas_encontradas WHERE id_mascota = {id_mascota};"
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

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)



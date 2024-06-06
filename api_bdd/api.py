from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root@lost_pets/lost_pets_db")

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

def crear_duenio(data_owner):
    conn = engine.connect()
    query = f"""INSERT INTO duenios (nombre, mail, telefono, barrio) 
                VALUES ('{data_owner["nombre"]}', '{data_owner["mail"]}', {data_owner["telefono"]}, '{data_owner["barrio"]}');"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201



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

def crear_informante(data_informant):
    conn = engine.connect()
    query = f"""INSERT INTO informante (nombre, telefono, barrio) 
                VALUES ('{data_informant["nombre"]}', {data_informant["telefono"]}, '{data_informant["barrio"]}');"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201


def obtener_informante(id_informant):
    conn = engine.connect()
    query = f"SELECT * FROM informante WHERE id_informante = {id_informant};"
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

def borrar_informante(id_informant):
    conn = engine.connect()
    query = f"DELETE FROM informante WHERE id_informante = {id_informant};"
    validation_query = f"SELECT * FROM informante WHERE id_informante = {id_informant};"
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
            'animal':row.animal,
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'tamanio': row.tamanio,
            'barrio': row.barrio,
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio
        }
        data.append(entity)

    return jsonify(data), 200

def crear_mascota_perdida(data_lost_pet):
    conn = engine.connect()
    query = f"""INSERT INTO mascotas_perdidas (raza, nombre, color, sexo, edad_aprox, tamanio, barrio, mail_duenio, telefono_duenio) 
                VALUES ('{data_lost_pet["animal"]}','{data_lost_pet["raza"]}', '{data_lost_pet["nombre"]}', '{data_lost_pet["color"]}', '{data_lost_pet["sexo"]}',
                        '{data_lost_pet["tamanio"]}', '{data_lost_pet["barrio"]}',
                        '{data_lost_pet["mail_duenio"]}', {data_lost_pet["telefono_duenio"]});"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201

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
            'telefono_duenio': row.telefono_duenio
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
            'animal':row.animal,
            'raza': row.raza,
            'nombre': row.nombre,
            'color': row.color,
            'sexo': row.sexo,
            'tamanio': row.tamanio,
            'barrio': row.barrio,
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio,
            'telefono_informante': row.telefono_informante,
            'id_informante': row.id_informante
        }
        data.append(entity)

    return jsonify(data), 200

def crear_mascota_encontrada(data_pet):
    conn = engine.connect()
    query = f"""INSERT INTO mascotas_encontradas (raza, nombre, color, sexo, tamanio, edad_aprox, barrio,
                mail_duenio, telefono_duenio, telefono_informante, id_informante) 
                VALUES ('{data_pet["animal"]}','{data_pet["raza"]}', '{data_pet["nombre"]}', '{data_pet["color"]}', 
                '{data_pet["sexo"]}', '{data_pet["tamanio"]}',
                '{data_pet["barrio"]}', '{data_pet["mail_duenio"]}', {data_pet["telefono_duenio"]},
                {data_pet["telefono_informante"]}, {data_pet["id_informante"]});"""
    try:
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

    return jsonify({'message': 'Se ha agregado correctamente'}), 201


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
            'mail_duenio': row.mail_duenio,
            'telefono_duenio': row.telefono_duenio,
            'telefono_informante': row.telefono_informante,
            'id_informante': row.id_informante
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

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)

"""
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root@localhost/ids")

def ejecutar_query(query):
    conn = engine.connect()
    try:
        resultado = conn.execute(text(query))
        conn.commit()
        return resultado
    except SQLAlchemyError as err:
        return str(err.__cause__)
    finally:
        conn.close()

def obtener_todo(tabla):
    query = f"SELECT * FROM {tabla};"
    resultadoado = ejecutar_query(query)
    data = [{column: value for column, value in row.items()} for row in resultadoado]
    return jsonify(data), 200

No se si funciona esto:
def crear_dato(tabla):
    new_record = request.get_json()
    columns = ', '.join(new_record.keys())
    values = ', '.join([f"'{value}'" for value in new_record.values()])
    query = f"INSERT INTO {tabla} ({columns}) VALUES ({values});"
    resultado = ejecutar_query(query)
    return jsonify({'message': f'Se ha agregado correctamente a {tabla}'}), 201

def actualizar_dato(tabla, id_tabla,id_busqueda):
    mod_record = request.get_json()
    update_values = ', '.join([f"{column} = '{value}'" for column, value in mod_record.items()])
    query = f"UPDATE {tabla} SET {update_values} WHERE {id_tabla} = {id_busqueda};"
    resultado = ejecutar_query(query)
    if resultado.rowcount == 0:
        return jsonify({"message": f"No se encontró el registro en {tabla}"}), 404
    return jsonify({'message': f'Se ha modificado correctamente en {tabla}'}), 200


def obtener_por_id(tabla, id_tabla,id_busqueda):
    query = f"SELECT * FROM {tabla} WHERE {id_tabla} = {id_busqueda};"
    resultado = ejecutar_query(query)
    if resultado.rowcount == 0:
        return jsonify({"message": "El registro no existe"}), 404
    data = [{column: value for column, value in row.items()} for row in resultado]
    return jsonify(data[0]), 200



def borrar_dato(tabla, id_tabla,id_busqueda):
    query = f"DELETE FROM {tabla} WHERE {id_tabla} = {id_busqueda};"
    resultado = ejecutar_query(query)
    if resultado.rowcount == 0:
        return jsonify({"message": f"No se encontró el registro en {tabla}"}), 404
    return jsonify({'message': f'Se ha eliminado correctamente de {tabla}'}), 200

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)
"""


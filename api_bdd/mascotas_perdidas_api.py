from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root@localhost/ids")

@app.route('/mascotas_perdidas', methods=['GET'])
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

@app.route('/create_mascota_perdida', methods=['POST'])
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

@app.route('/mascotas_perdidas/<id_mascota>', methods=['PATCH'])
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

@app.route('/mascotas_perdidas/<id_mascota>', methods=['GET'])
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

@app.route('/mascotas_perdidas/<id_mascota>', methods=['DELETE'])
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

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)


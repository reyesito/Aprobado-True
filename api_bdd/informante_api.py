from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root@localhost/ids")

@app.route('/informantes', methods=['GET'])
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

@app.route('/create_informante', methods=['POST'])
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

@app.route('/informantes/<id_informante>', methods=['PATCH'])
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

@app.route('/informantes/<id_informante>', methods=['GET'])
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

@app.route('/informantes/<id_informante>', methods=['DELETE'])
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

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)



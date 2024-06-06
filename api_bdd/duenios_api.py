from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root@localhost/ids")

@app.route('/duenios', methods=['GET'])
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

@app.route('/create_duenio', methods=['POST'])
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

@app.route('/duenios/<id_duenio>', methods=['PATCH'])
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

@app.route('/duenios/<id_duenio>', methods=['GET'])
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

@app.route('/duenios/<id_duenio>', methods=['DELETE'])
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

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root:12345@localhost/lost_pets_db")


@app.route('/duenios', methods=['GET'])
def obtener_duenios():
    conn = engine.connect()
    query = "SELECT * FROM duenios;"
    try:
        result = conn.execute(text(query))
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
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify(data), 200

@app.route('/crear_duenio', methods=['POST'])
def crear_duenio():
    conn = engine.connect()
    new_owner = request.get_json()
    query = text("""
        INSERT INTO duenios (nombre, mail, telefono, barrio)
        VALUES (:nombre, :mail, :telefono, :barrio);
    """)
    try:
        conn.execute(query, nombre=new_owner["nombre"], mail=new_owner["mail"], telefono=new_owner["telefono"], barrio=new_owner["barrio"])
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha agregado correctamente'}), 201

@app.route('/duenios/<id_duenio>', methods=['PATCH'])
def actualizar_duenio(id_duenio):
    conn = engine.connect()
    mod_owner = request.get_json()
    query = text("""
        UPDATE duenios SET
            nombre = :nombre,
            mail = :mail,
            telefono = :telefono,
            barrio = :barrio
        WHERE id_duenio = :id_duenio;
    """)
    query_validation = text("SELECT * FROM duenios WHERE id_duenio = :id_duenio;")
    try:
        val_result = conn.execute(query_validation, id_duenio=id_duenio)
        if val_result.rowcount == 0:
            return jsonify({'message': "El dueño no existe"}), 404
        conn.execute(query, id_duenio=id_duenio, nombre=mod_owner.get('nombre'), mail=mod_owner.get('mail'), telefono=mod_owner.get('telefono'), barrio=mod_owner.get('barrio'))
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify({'message': str(err.__cause__)}), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha modificado correctamente'}), 200

@app.route('/duenios/<id_duenio>', methods=['GET'])
def obtener_duenio(id_duenio):
    conn = engine.connect()
    query = text("SELECT * FROM duenios WHERE id_duenio = :id_duenio;")
    try:
        result = conn.execute(query, id_duenio=id_duenio)
        row = result.fetchone()
        if row:
            data = {
                'id_duenio': row.id_duenio,
                'nombre': row.nombre,
                'mail': row.mail,
                'telefono': row.telefono,
                'barrio': row.barrio
            }
        else:
            return jsonify({"message": "El dueño no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify(data), 200

@app.route('/duenios/<id_duenio>', methods=['DELETE'])
def borrar_duenio(id_duenio):
    conn = engine.connect()
    query = text("DELETE FROM duenios WHERE id_duenio = :id_duenio;")
    validation_query = text("SELECT * FROM duenios WHERE id_duenio = :id_duenio")
    try:
        val_result = conn.execute(validation_query, id_duenio=id_duenio)
        if val_result.rowcount == 0:
            return jsonify({"message": "El dueño no existe"}), 404
        conn.execute(query, id_duenio=id_duenio)
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha eliminado correctamente'}), 202
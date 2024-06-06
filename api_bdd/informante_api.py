from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root:12345@localhost/lost_pets_db")


@app.route('/informantes', methods=['GET'])
def obtener_informantes():
    conn = engine.connect()
    query = "SELECT * FROM informante;"
    try:
        result = conn.execute(text(query))
        data = []
        for row in result:
            entity = {
                'id_informante': row.id_informante,
                'nombre': row.nombre,
                'telefono': row.telefono,
                'barrio': row.barrio
            }
            data.append(entity)
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify(data), 200

@app.route('/crear_informante', methods=['POST'])
def crear_informante():
    conn = engine.connect()
    new_informant = request.get_json()
    query = text("""
        INSERT INTO informante (nombre, telefono, barrio)
        VALUES (:nombre, :telefono, :barrio);
    """)
    try:
        conn.execute(query, nombre=new_informant["nombre"], telefono=new_informant["telefono"], barrio=new_informant["barrio"])
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha agregado correctamente'}), 201

@app.route('/informantes/<id_informante>', methods=['PATCH'])
def actualizar_informante(id_informante):
    conn = engine.connect()
    mod_informant = request.get_json()
    query = text("""
        UPDATE informante SET
            nombre = :nombre,
            telefono = :telefono,
            barrio = :barrio
        WHERE id_informante = :id_informante;
    """)
    query_validation = text("SELECT * FROM informante WHERE id_informante = :id_informante;")
    try:
        val_result = conn.execute(query_validation, id_informante=id_informante)
        if val_result.rowcount == 0:
            return jsonify({'message': "El informante no existe"}), 404
        conn.execute(query, id_informante=id_informante, nombre=mod_informant.get('nombre'), telefono=mod_informant.get('telefono'), barrio=mod_informant.get('barrio'))
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify({'message': str(err.__cause__)}), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha modificado correctamente'}), 200

@app.route('/informantes/<id_informante>', methods=['GET'])
def obtener_informante(id_informante):
    conn = engine.connect()
    query = text("SELECT * FROM informante WHERE id_informante = :id_informante;")
    try:
        result = conn.execute(query, id_informante=id_informante)
        row = result.fetchone()
        if row:
            data = {
                'id_informante': row.id_informante,
                'nombre': row.nombre,
                'telefono': row.telefono,
                'barrio': row.barrio
            }
        else:
            return jsonify({"message": "El informante no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify(data), 200

@app.route('/informantes/<id_informante>', methods=['DELETE'])
def borrar_informante(id_informante):
    conn = engine.connect()
    query = text("DELETE FROM informante WHERE id_informante = :id_informante;")
    validation_query = text("SELECT * FROM informante WHERE id_informante = :id_informante")
    try:
        val_result = conn.execute(validation_query, id_informante=id_informante)
        if val_result.rowcount == 0:
            return jsonify({"message": "El informante no existe"}), 404
        conn.execute(query, id_informante=id_informante)
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha eliminado correctamente'}), 202

if __name__ == '__main__':
    app.run(debug=True)


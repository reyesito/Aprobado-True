from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root:12345@localhost/lost_pets_db")

@app.route('/duenios', methods=['GET'])
def get_owners():
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
def create_owner():
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
def update_owner(id_duenio):
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
def get_owner(id_duenio):
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
def delete_owner(id_duenio):
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

@app.route('/informantes', methods=['GET'])
def get_informants():
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

@app.route('/mascotas_perdidas', methods=['GET'])
def get_lost_pets():
    conn = engine.connect()
    query = "SELECT * FROM mascotas_perdidas;"
    try:
        result = conn.execute(text(query))
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
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify(data), 200

if __name__ == "__main__":
    app.run("0.0.0.0", port="5000", debug=True)


@app.route('/mascotas_perdidas', methods=['DELETE'])
def delete_mascota(id_mascota):
    conn = engine.connect()
    query = text("DELETE FROM mascotas WHERE id_mascota = :id_mascota;")
    validation_query = text("SELECT * FROM mascotas WHERE id_mascotas = :id_mascotas")
    try:
        val_result = conn.execute(validation_query, id_mascota=id_mascota)
        if val_result.rowcount == 0:
            return jsonify({"message": "La mascota no existe"}), 404
        conn.execute(query, id_mascota = id_mascota)
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha eliminado correctamente'}), 202

@app.route('/mascotas_perdidas', methods=['POST'])
def create_mascota_perdida():
    conn = engine.connect()
    new_pet = request.get_json()
    query = text("""
        INSERT INTO mascotas_perdidas (color, raza, nombre, sexo, edad_aprox, tamanio, barrio, mail_duenio, telefono_duenio)
        VALUES (:color, :raza, :nombre, :sexo, :edad_aprox, :tamanio, :mail_duenio, :telefono_duenio);
    """)
    try:
        conn.execute(query, color=new_pet["color"], raza=new_pet["raza"], nombre=new_pet["nombre"],
                     sexo=new_pet["sexo"], edad_aprox=new_pet["edad_aprox"], tamanio=new_pet["tamanio"],
                     mail_duenio=new_pet["mail_duenio"], telefono_duenio=new_pet["telefono_duenio"])
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha agregado correctamente'}), 201



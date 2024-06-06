from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root:12345@localhost/lost_pets_db")


@app.route('/mascotas_perdidas', methods=['GET'])
def obtener_mascotas_perdidas():
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

@app.route('/crear_mascota_perdida', methods=['POST'])
def crear_mascotas_perdidas():
    conn = engine.connect()
    new_pet = request.get_json()
    query = text("""
        INSERT INTO mascotas_perdidas (raza, nombre, color, sexo, edad_aprox, tamanio, barrio, mail_duenio, telefono_duenio)
        VALUES (:raza, :nombre, :color, :sexo, :edad_aprox, :tamanio, :barrio, :mail_duenio, :telefono_duenio);
    """)
    try:
        conn.execute(query, raza=new_pet["raza"], nombre=new_pet["nombre"], color=new_pet["color"], sexo=new_pet["sexo"], edad_aprox=new_pet["edad_aprox"], tamanio=new_pet["tamanio"], barrio=new_pet["barrio"], mail_duenio=new_pet["mail_duenio"], telefono_duenio=new_pet["telefono_duenio"])
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha agregado correctamente'}), 201

@app.route('/mascotas_perdidas/<id_mascota>', methods=['PATCH'])
def actualizar_mascota_perdida(id_mascota):
    conn = engine.connect()
    mod_pet = request.get_json()
    query = text("""
        UPDATE mascotas_perdidas SET
            raza = :raza,
            nombre = :nombre,
            color = :color,
            sexo = :sexo,
            edad_aprox = :edad_aprox,
            tamanio = :tamanio,
            barrio = :barrio,
            mail_duenio = :mail_duenio,
            telefono_duenio = :telefono_duenio
        WHERE id_mascota = :id_mascota;
    """)
    query_validation = text("SELECT * FROM mascotas_perdidas WHERE id_mascota = :id_mascota;")
    try:
        val_result = conn.execute(query_validation, id_mascota=id_mascota)
        if val_result.rowcount == 0:
            return jsonify({'message': "La mascota no existe"}), 404
        conn.execute(query, id_mascota=id_mascota, raza=mod_pet.get('raza'), nombre=mod_pet.get('nombre'), color=mod_pet.get('color'), sexo=mod_pet.get('sexo'), edad_aprox=mod_pet.get('edad_aprox'), tamanio=mod_pet.get('tamanio'), barrio=mod_pet.get('barrio'), mail_duenio=mod_pet.get('mail_duenio'), telefono_duenio=mod_pet.get('telefono_duenio'))
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify({'message': str(err.__cause__)}), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha modificado correctamente'}), 200

@app.route('/mascotas_perdidas/<id_mascota>', methods=['GET'])
def obtener_mascota_perdida(id_mascota):
    conn = engine.connect()
    query = text("SELECT * FROM mascotas_perdidas WHERE id_mascota = :id_mascota;")
    try:
        result = conn.execute(query, id_mascota=id_mascota)
        row = result.fetchone()
        if row:
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
        else:
            return jsonify({"message": "La mascota no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify(data), 200

@app.route('/mascotas_perdidas/<id_mascota>', methods=['DELETE'])
def borrar_mascota_perdida(id_mascota):
    conn = engine.connect()
    query = text("DELETE FROM mascotas_perdidas WHERE id_mascota = :id_mascota;")
    validation_query = text("SELECT * FROM mascotas_perdidas WHERE id_mascota = :id_mascota")
    try:
        val_result = conn.execute(validation_query, id_mascota=id_mascota)
        if val_result.rowcount == 0:
            return jsonify({"message": "La mascota no existe"}), 404
        conn.execute(query, id_mascota=id_mascota)
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha eliminado correctamente'}), 202

if __name__ == '__main__':
    app.run(debug=True)

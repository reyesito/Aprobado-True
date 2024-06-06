from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root:12345@localhost/lost_pets_db")


@app.route('/mascotas_encontradas', methods=['GET'])
def obtener_mascotas_encontradas():
    conn = engine.connect()
    query = "SELECT * FROM mascotas_encontradas;"
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
                'tamanio': row.tamanio,
                'edad_aprox': row.edad_aprox,
                'barrio': row.barrio,
                'mail_duenio': row.mail_duenio,
                'telefono_duenio': row.telefono_duenio,
                'telefono_informante': row.telefono_informante,
                'id_informante': row.id_informante
            }
            data.append(entity)
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify(data), 200

@app.route('/crear_mascota_encontrada', methods=['POST'])
def crear_mascota_encontrada():
    conn = engine.connect()
    new_pet = request.get_json()
    query = text("""
        INSERT INTO mascotas_encontradas (raza, nombre, color, sexo, tamanio, edad_aprox, barrio, mail_duenio, telefono_duenio, telefono_informante, id_informante)
        VALUES (:raza, :nombre, :color, :sexo, :tamanio, :edad_aprox, :barrio, :mail_duenio, :telefono_duenio, :telefono_informante, :id_informante);
    """)
    try:
        conn.execute(query, raza=new_pet["raza"], nombre=new_pet["nombre"], color=new_pet["color"], sexo=new_pet["sexo"], tamanio=new_pet["tamanio"], edad_aprox=new_pet["edad_aprox"], barrio=new_pet["barrio"], mail_duenio=new_pet["mail_duenio"], telefono_duenio=new_pet["telefono_duenio"], telefono_informante=new_pet["telefono_informante"], id_informante=new_pet["id_informante"])
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha agregado correctamente'}), 201

@app.route('/mascotas_encontradas/<id_mascota>', methods=['PATCH'])
def obtener_mascota_encontrada(id_mascota):
    conn = engine.connect()
    mod_pet = request.get_json()
    query = text("""
        UPDATE mascotas_encontradas SET
            raza = :raza,
            nombre = :nombre,
            color = :color,
            sexo = :sexo,
            tamanio = :tamanio,
            edad_aprox = :edad_aprox,
            barrio = :barrio,
            mail_duenio = :mail_duenio,
            telefono_duenio = :telefono_duenio,
            telefono_informante = :telefono_informante,
            id_informante = :id_informante
        WHERE id_mascota = :id_mascota;
    """)
    query_validation = text("SELECT * FROM mascotas_encontradas WHERE id_mascota = :id_mascota;")
    try:
        val_result = conn.execute(query_validation, id_mascota=id_mascota)
        if val_result.rowcount == 0:
            return jsonify({'message': "La mascota no existe"}), 404
        conn.execute(query, id_mascota=id_mascota, raza=mod_pet.get('raza'), nombre=mod_pet.get('nombre'), color=mod_pet.get('color'), sexo=mod_pet.get('sexo'), tamanio=mod_pet.get('tamanio'), edad_aprox=mod_pet.get('edad_aprox'), barrio=mod_pet.get('barrio'), mail_duenio=mod_pet.get('mail_duenio'), telefono_duenio=mod_pet.get('telefono_duenio'), telefono_informante=mod_pet.get('telefono_informante'), id_informante=mod_pet.get('id_informante'))
        conn.commit()
    except SQLAlchemyError as err:
        return jsonify({'message': str(err.__cause__)}), 500
    finally:
        conn.close()
    return jsonify({'message': 'Se ha modificado correctamente'}), 200

@app.route('/mascotas_encontradas/<id_mascota>', methods=['GET'])
def obtener_mascota_encontrada(id_mascota):
    conn = engine.connect()
    query = text("SELECT * FROM mascotas_encontradas WHERE id_mascota = :id_mascota;")
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
                'tamanio': row.tamanio,
                'edad_aprox': row.edad_aprox,
                'barrio': row.barrio,
                'mail_duenio': row.mail_duenio,
                'telefono_duenio': row.telefono_duenio,
                'telefono_informante': row.telefono_informante,
                'id_informante': row.id_informante
            }
        else:
            return jsonify({"message": "La mascota no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)), 500
    finally:
        conn.close()
    return jsonify(data), 200

@app.route('/mascotas_encontradas/<id_mascota>', methods=['DELETE'])
def borrar_mascota_encontrada(id_mascota):
    conn = engine.connect()
    query = text("DELETE FROM mascotas_encontradas WHERE id_mascota = :id_mascota;")
    validation_query = text("SELECT * FROM mascotas_encontradas WHERE id_mascota = :id_mascota")
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


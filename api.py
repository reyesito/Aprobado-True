from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root:12345@lost_pets/lost_pets_db")


@app.route('/users', methods = ['GET'])
def users():
    conn = engine.connect()
    
    query = "SELECT * FROM users;"
    try:
        #Se debe usar text para poder adecuarla al execute de mysql-connector
        result = conn.execute(text(query))
        #Se hace commit de la consulta (acá no estoy seguro si es necesario para un select, sí es necesario para un insert!)
        conn.close() #Cerramos la conexion con la base de datos
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    
    #Se preparan los datos para ser mostrador como json
    data = []
    for row in result:
        entity = {}
        entity['id'] = row.id
        entity['name'] = row.name
        entity['email'] = row.email
        entity['created_at'] = row.created_at
        data.append(entity)

    return jsonify(data), 200


@app.route('/create_user', methods = ['POST'])
def create_user():
    conn = engine.connect()
    new_user = request.get_json()
    #Se crea la query en base a los datos pasados por el endpoint.
    #Los mismos deben viajar en el body en formato JSON
    query = f"""INSERT INTO users (name, email) VALUES ('{new_user["name"]}', '{new_user["email"]}');"""
    try:
        result = conn.execute(text(query))
        #Una vez ejecutada la consulta, se debe hacer commit de la misma para que
        #se aplique en la base de datos.
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message': 'Se ha producido un error' + str(err.__cause__)})
    
    return jsonify({'message': 'se ha agregado correctamente' + query}), 201



@app.route('/users/<id>', methods = ['PATCH'])
def update_user(id):
    conn = engine.connect()
    mod_user = request.get_json()
    #De la misma manera que con el metodo POST los datos a modificar deberán
    #Ser enviados por medio del body de la request
    query = f"""UPDATE users SET name = '{mod_user['name']}'
                {f", email = '{mod_user['email']}'" if "email" in mod_user else ""}
                WHERE id = {id};
            """
    query_validation = f"SELECT * FROM users WHERE id = {id};"
    try:
        val_result = conn.execute(text(query_validation))
        if val_result.rowcount!=0:
            result = conn.execute(text(query))
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({'message': "El usuario no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify({'message': str(err.__cause__)})
    return jsonify({'message': 'se ha modificado correctamente' + query}), 200

@app.route('/users/<id>', methods = ['GET'])
def get_user(id):
    conn = engine.connect()
    query = f"""SELECT *
            FROM users
            WHERE id = {id};
            """
    try:
        result = conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    if result.rowcount !=0:
        data = {}
        row = result.first()
        data['id'] = row[0]
        data['name'] = row[1]
        data['email'] = row[2]
        data['created_at'] = row[3]
        return jsonify(data), 200
    return jsonify({"message": "El usuario no existe"}), 404


@app.route('/users/<id>', methods = ['DELETE'])
def delete_user(id):
    conn = engine.connect()
    query = f"""DELETE FROM users
            WHERE id = {id};
            """
    validation_query = f"SELECT * FROM users WHERE id = {id}"
    try:
        val_result = conn.execute(text(validation_query))
        if val_result.rowcount != 0 :
            result = conn.execute(text(query))
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({"message": "El usuario no existe"}), 404
    except SQLAlchemyError as err:
        jsonify(str(err.__cause__))
    return jsonify({'message': 'Se ha eliminado correctamente'}), 202


if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)
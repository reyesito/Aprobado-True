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

""" No se si funciona esto:
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
"""

def obtener_por_id(tabla, id_tabla,id_busqueda):
    query = f"SELECT * FROM {tabla} WHERE {id_tabla} = {id_busqueda};"
    resultado = ejecutar_query(query)
    if resultado.rowcount == 0:
        return jsonify({"message": "El registro no existe"}), 404
    data = [{column: value for column, value in row.items()} for row in resultado]
    return jsonify(data[0]), 200



def borrar_dato(tabla, id_tabla,id_busqueda):
    query = f"DELETE FROM {tabla} WHERE id = {id};"
    resultado = ejecutar_query(query)
    if resultado.rowcount == 0:
        return jsonify({"message": f"No se encontró el registro en {tabla}"}), 404
    return jsonify({'message': f'Se ha eliminado correctamente de {tabla}'}), 200

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)

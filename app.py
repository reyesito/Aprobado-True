from flask import Flask, jsonify, render_template, request, redirect, url_for
#dependencias para subir archivos(fotos)
from werkzeug.utils import secure_filename
import os
from os import path

#from api import *
from file_api.found_pets import *
from file_api.informants import *
from file_api.lost_pets import *
from file_api.map import *
from file_api.owners import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

#renderizado de listados

@app.route("/lista-mascotas-encontradas")
def lista_masc_encontradas():
    try:
        data = obtener_mascotas_encontradas()
        listado = listar_fotos("static/pets/encontrados")
        return render_template("lista-masc-encontradas.html", data=data, fotos=listado)
    except Exception as e:
        return f'Error al obtener mascotas encontradas: {str(e)}'


@app.route('/lista-mascotas-perdidas')
def lista_masc_perdidas():
    try:
        data = obtener_mascotas_perdidas()
        listado = listar_fotos("static/pets/perdidos")
        return render_template("lista-masc-perdidas.html", data=data, fotos=listado)
    except Exception as e:
        return f'Error al obtener mascotas encontradas: {str(e)}'

#FORMULARIO DE MASCOTA EMCONTRADA
@app.route("/registro_encontrado")
def registro_encontrado():
    try:
        data = obtener_mascotas_encontradas()
        listado = listar_fotos("static/pets/encontrados")
        return render_template("mascota-encontrada.html", data=data, fotos=listado)
    except Exception as e:
        return f'Error al obtener mascotas encontradas: {str(e)}'

@app.route("/encontrado", methods=["POST"])
def encontrado():
    if request.method == "POST":
        user_name = request.form.get("fname")
        pet_name = request.form.get("fpetname")
        animal = request.form.get("fanimal")
        type_class = request.form.get("ftype")
        color = request.form.get("fcolor")
        sex = request.form.get("fsex")
        size = request.form.get("fsize")
        city = request.form.get("fcity")
        mail = request.form.get("fmail")
        telephone = request.form.get("ftel")
        latitude = request.form.get("flatitude")
        longitude = request.form.get("flongitude")
        
        new_informant = {
            "user_name": user_name,
            "mail": mail,
            "telephone": telephone,
            "city": city
        }
        
        found_pet = {
            "pet_name": pet_name,
            "animal": animal,
            "type_class": type_class,
            "color": color,
            "sex": sex,
            "size": size,
            "telephone": telephone,
            "mail": mail,
            "latitude": latitude,
            "longitude": longitude
        }
        
        crear_informante(new_informant)
        crear_mascota_encontrada(found_pet)

        # Guardar la foto en el servidor
        # id = obtener_id_encontrado(found_pet)  # HACER FUNCIÓN EN API
        foto = request.files['ffoto']
        basepath = path.dirname(__file__)
        filename = secure_filename(foto.filename)

        extension = filename.split(".")[1]
        new_name = f"{id}.{extension}"

        upload_path = path.join(basepath, 'static/pets/encontrados', new_name)
        foto.save(upload_path)

        return redirect(url_for("lista_masc_encontradas"))

    return render_template('mascota-encontrada.html')


#FORMULARIO DE MASCOTA PERDIDA

@app.route("/registro_perdido")
def registro_perdido():
    try:
        data = obtener_mascotas_perdidas()
        listado = listar_fotos("static/pets/perdidos")
        return render_template("mascota-perdida.html", data=data, fotos=listado)
    except Exception as e:
        return f'Error al obtener mascotas perdidas: {str(e)}'

@app.route("/perdido", methods=["POST"])
def perdido():
    if request.method == "POST":
        user_name = request.form.get("fname")
        pet_name = request.form.get("fpetname")
        animal = request.form.get("fanimal")
        type_class = request.form.get("ftype")
        color = request.form.get("fcolor")
        sex = request.form.get("fsex")
        size = request.form.get("fsize")
        city = request.form.get("fcity")
        mail = request.form.get("fmail")
        telephone = request.form.get("ftel")

        new_owner = {
            "user_name": user_name,
            "mail": mail,
            "telephone": telephone,
            "city": city
        }
        new_lost_pet = {
            "pet_name": pet_name,
            "animal": animal,
            "type_class":type_class,
            "color":color,
            "sex":sex,
            "size":size,
            "city":city,
            "telephone":telephone,
            "mail": mail
        }
        print(new_lost_pet)
        crear_duenio(new_owner)
        crear_mascota_perdida(new_lost_pet)

        #guardar la foto en el servidor
        #id = obtener_id_perdido(new_lost_pet) #-------------------------------------HACER FUNCION EN API------------
        foto = request.files['ffoto']
        basepath = path.dirname(__file__)
        filename = secure_filename(foto.filename)

        extension = filename.split(".")[1]
        new_name = f"{id}.{extension}"

        upload_path = path.join(basepath, 'static/pets/perdidos', new_name)
        foto.save(upload_path)

        return redirect(url_for("lista_masc_perdidas"))
    return render_template('mascota-perdida.html')

#funciones de borrado de datos de bbdd:

@app.route("/borrar/perdido/<id>")
def borrar_perdido(id):
    borrar_mascota_perdida(id)
    borrar_duenio(id)
    return redirect(url_for("lista_perdidos"))

@app.route("/borrar/encontrado/<id>")
def borrar_encontrado(id):
    borrar_mascota_encontrada(id)
    borrar_informante(id)
    return redirect(url_for("listado_encontrados"))

#renderizado de mapa
@app.route("/mapa")
def mapa():
    return render_template('mapa.html')

@app.route("/api/coordenadas")
def api_coordenadas():
    data, status_code = obtener_coordenadas()
    return data, status_code

#renderizado de errores
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

#funcion auxiliar
def listar_fotos(ruta):
    listado = {}
    for foto in os.listdir(ruta):
        filename = foto.split(".")[0]
        listado[filename] = foto
    return listado

if __name__ == "__main__":
    app.run("127.0.0.1", port=5001, debug=True)
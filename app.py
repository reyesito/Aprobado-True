from flask import Flask, jsonify, render_template, request, redirect, url_for
from api import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def mascota_encontrada():
    return render_template('mascota-encontrada.html')

@app.route("/registro")
def mascota_perdida():
    return render_template('mascota-perdida.html')

@app.route("/reportado", methods=["POST"])
def reportado():
    if request.method == "POST":
        user_name = request.form.get ("fname")
        pet_name = request.form.get("fpetname")
        animal = request.form.get("fanimal")
        type_class = request.form.get("ftype")
        color = request.form.get("fcolor")
        sex = request.form.get("fsex")
        size = request.form.get("fsize")
        city = request.form.get("fcity")
        mail = request.form.get("fmail")
        telephone = request.form.get("ftel")
        new_informant = { 
            "user_name" : user_name,
            "mail" : mail,
            "telephone" : telephone,
            "city": city 
        }
        found_pet = {
            "pet_name": pet_name,
            "animal": animal,
            "type_class": type_class,
            "color": color,
            "sex": sex,
            "size": size,
            "city": city,
            "telephone": telephone
        }
        crear_informante(new_informant)
        crear_mascota_encontrada(found_pet)

    return redirect(url_for("home"))

@app.route("/registrado", methods=["POST"])
def registrado():
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
            "telephone":telephone
        }
        crear_duenio(new_owner)
        crear_mascota_perdida(new_lost_pet)
    
    return redirect(url_for("home"))
'''
@app.route("", methods=["GET"])
def obtener_lista_duenios():
    return obtener_duenios()

@app.route("", methods=["GET"])
def obtener_un_duenio(id_owner):
    return obtener_duenio(id_owner)

@app.route("", methods=["DELETE"])
def borrar_un_duenio(id_owner):
    return borrar_duenio(id_owner)

@app.route("", methods=["GET"])
def obtener_lista_informantes():
    return obtener_informantes()

@app.route("", methods=["GET"])
def obtener_un_informante(id_informant):
    return obtener_informante(id_informant)

@app.route("", methods=["DELETE"])
def borrar_un_informante(id_informant):
    return borrar_informante(id_informant)

@app.route("", methods=["GET"])
def obtener_lista_mascotas_perdidas():
    return obtener_mascotas_perdidas()

@app.route("", methods=["GET"])
def obtener_una_mascota_perdida(id_lost_pet):
    return obtener_mascota_perdida(id_lost_pet)

@app.route("", methods=["DELETE"])
def borrar_una_mascota_perdida(id_lost_pet):
    return borrar_mascota_perdida(id_lost_pet)

@app.route("", methods=["GET"])
def obtener_lista_mascotas_encontradas():
    return obtener_mascotas_encontradas()

@app.route("", methods=["GET"])
def obtener_una_mascota_encontrada(id_pet):
    return obtener_mascota_encontrada(id_pet)

@app.route("", methods=["DELETE"])
def borrar_una_mascota_encontrada(id_pet):
    return borrar_mascota_encontrada(id_pet)
'''

@app.route("/listado")
def listado():
    return render_template("listado.html")
@app.route("/mapa")
def mapa():
    return render_template('mapa.html')

if __name__ == "__main__":
    app.run("127.0.0.1", port=5001, debug=True)
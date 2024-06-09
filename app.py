from flask import Flask, jsonify, render_template, request, redirect, url_for
from api import (obtener_mascotas_encontradas, obtener_mascotas_perdidas, obtener_coordenadas,
                 crear_mascota_perdida, crear_mascota_encontrada, crear_informante, crear_duenio,
                 borrar_mascota_perdida, borrar_mascota_encontrada, borrar_informante, borrar_duenio)

app = Flask(__name__)
#renderizado de rutas:
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/registro")
def registro():
    return render_template('registro.html')

@app.route("/map")#no se si <coordenadas> es necesario
def map():
    response = obtener_coordenadas()
    data = []
    if response.status_code == 200:
        data = response.json()
    else:
        print(f'error: {response.status_code}')
    return render_template('mapa.html', coordenadas=data)

@app.route("/listado/perdidas") #no se si <data> es necesario
def listado_perdidos():
    response = obtener_mascotas_perdidas()
    data = []
    if response.status_code == 200:
        data = response.json()
    else:
        return print(f'error: {response.status_code}')
    return render_template("lista-masc-perdidas.html", data=data)

@app.route("/listado/encontradas") #no se si <data> es necesario
def listado_encontrados():
    response = obtener_mascotas_encontradas()
    if response.status_code == 200:
        data = response.json()
    else:
        return print(f'error: {response.status_code}')
    return render_template("lista-masc-encontradas.html", data=data)

#funciones de ingreso de datos a bbdd:
@app.route("/reportado", methods=["POST"])
def reportado():
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
            "city": city,
            "telephone": telephone,
            "mail": mail
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
            "type_class": type_class,
            "color": color,
            "sex": sex,
            "size": size,
            "city": city,
            "telephone": telephone,
            "mail": mail
        }
        crear_duenio(new_owner)
        crear_mascota_perdida(new_lost_pet)

    return redirect(url_for("home"))

#funciones de borrado de datos de bbdd:

@app.route("/borrar/perdido/<id>"):
def borrar_perdido(id):
    borrar_mascota_perdida(id)
    borrar_duenio(id)
    return redirect(url_for("lista_perdidos"))

@app.route("/borrar/encontrado/<id>"):
def borrar_encontrado(id):
    borrar_mascota_encontrada(id)
    borrar_informante(id)
    return redirect(url_for("listado_encontrados"))


#renderizado de errores
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

"""
@app.route("/exito/<nombre>-<email>-<msg>")
def exito(nombre, email, msg):
    #print(nombre)
    #print(email)
    #print(msg)
    return render_template("exito.html", nombre=nombre, email=email, msg=msg)

@app.route("/contact", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        nombre = request.form.get("fname")
        mail = request.form.get("femail")
        msg = request.form.get("fmsg")
        return redirect(url_for("exito", nombre=nombre, email=mail, msg=msg))
    return render_template('contact.html')
"""

if __name__ == "__main__":
    app.run("127.0.0.1", port=5001, debug=True)
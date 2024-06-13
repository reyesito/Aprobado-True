from flask import Flask, jsonify, render_template, request, redirect, url_for
from api import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/lista-mascotas-encontradas")
def lista_masc_encontradas():
    try:
        data = obtener_mascotas_encontradas()
        return render_template("lista-masc-encontradas.html", data=data)
    except Exception as e:
        return f'Error al obtener mascotas encontradas: {str(e)}'

#esto pasa los datos como json
@app.route('/api/mascotas-encontradas')
def api_mascotas_encontradas():
    try:
        data = obtener_mascotas_encontradas()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 

#esto pasa los datos como json
@app.route('/api/mascotas-perdidas')
def api_mascotas_perdidas():
    try:
        data = obtener_mascotas_perdidas()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 

@app.route('/lista-mascotas-perdidas')
def lista_masc_perdidas():
    try:
        data = obtener_mascotas_perdidas()
        return render_template("lista-masc-perdidas.html", data=data)
    except Exception as e:
        return f'Error al obtener mascotas encontradas: {str(e)}'

"""

@app.route("/lista-mascotas-perdidas")
def lista_masc_perdidas():
    return render_template("lista-masc-perdidas.html")
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
"""
@app.route("/registro_encontrado")
def registro_encontrado():
    return render_template('mascota-encontrada.html')

@app.route("/encontrado", methods=["POST"])
def encontrado():
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
            "telephone": telephone,
            "mail": mail
        }
        crear_informante(new_informant)
        crear_mascota_encontrada(found_pet)

        return redirect(url_for("lista_masc_encontradas"))
    
    return render_template('mascota-encontrada.html')

@app.route("/registro_perdido")
def registro_perdido():
    return render_template('mascota-perdida.html')

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

#renderizado de errores
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route("/mapa")
def mapa():
    return render_template('mapa.html')

@app.route("/api/coordenadas")
def api_coordenadas():
    data, status_code = obtener_coordenadas()
    return data, status_code


if __name__ == "__main__":
    app.run("127.0.0.1", port=5001, debug=True)
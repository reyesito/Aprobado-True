from flask import Flask, jsonify, render_template, request, redirect, url_for
"""from api import *"""
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/map")
def map():

    return render_template('mapa.html')

@app.route("/registro")
def registro():
        return render_template('registro.html')

@app.route("/registrado", methods=["POST"])
def registrado():
    if request.method == "POST":
        name = request.form.get("fname")
        registrar(name, name_pet, email, contact, city)
    return redirect(url_for("home"))

@app.route("/listado")
def listado():
    return render_template("listado.html")
"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


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

"""
# Prueba no mas de guardar marcadores
@app.route('/guardar_marcadores', methods=['POST'])
def guardar_marcadores():
    if request.method == 'POST':
        marcadores = request.json  # Recibe los datos de marcadores en formato JSON
        //depende como se quiera procesar aca, podriamos usar base de datos, esto solo lo muestra en mensaje
        return jsonify({'message': 'Datos de marcadores recibidos correctamente', 'marcadores': marcadores})
"""
@app.route("/mapa")
def mapa():
    return render_template('mapa.html')



if __name__ == "__main__":
    app.run("127.0.0.1", port=5001, debug=True)
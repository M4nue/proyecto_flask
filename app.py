from flask import Flask, render_template, request
from static import funciones
archivo_json = funciones.cargar_json()
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/buscador')
def buscador():
    return render_template("buscador.html")

@app.route('/lista', methods=["post"])
def lista():
    nombre=request.form.get("Caja")
    
    if nombre == archivo_json["nombre"]:
        return render_template("lista.html", nombre=archivo_json["nombre"], precio=archivo_json["precio_compra"], imagen=archivo_json["imagen"])
    elif nombre == "":
        for i in archivo_json:
           return render_template("lista.html", nombre=i["nombre"], precio=i["precio_compra"], imagen=i["imagen"])
    else:
        return print('La caja',nombre,'no existe') 

app.run("0.0.0.0",5000,debug=True)
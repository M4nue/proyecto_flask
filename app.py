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
    nombre = request.form.get("Caja")
    coincidencias_nombres_caja = []
    precio_compra = []
    precio_venta = []

    for caja in archivo_json:
        if nombre == caja["nombre"]:
            return render_template("lista.html", nombre=caja["nombre"], precio_compra=caja["precio_compra"], precio_venta=caja["sale_price_text"])
        else:
            coincidencias_nombres_caja.append(caja["nombre"])
            precio_compra.append(caja["precio_compra"])
            precio_venta.append(caja["sale_price_text"])
    return render_template("lista.html", cajas=coincidencias_nombres_caja, precio_compra=precio_compra,precio_venta=precio_venta) 


app.run("0.0.0.0",5000,debug=True)
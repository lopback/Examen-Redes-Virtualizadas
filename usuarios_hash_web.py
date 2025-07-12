import sqlite3
import hashlib
from flask import Flask, request, redirect, render_template_string

# Crear la base de datos y tabla si no existe
def crear_base_datos():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            hash_clave TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Agregar usuarios con clave hasheada
def agregar_usuario(nombre, clave):
    hash_clave = hashlib.sha256(clave.encode()).hexdigest()
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, hash_clave) VALUES (?, ?)", (nombre, hash_clave))
    conn.commit()
    conn.close()

# Validar usuario ingresado en login
def validar_usuario(nombre, clave):
    hash_clave = hashlib.sha256(clave.encode()).hexdigest()
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND hash_clave = ?", (nombre, hash_clave))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

# Crear base y agregar usuarios (solo la primera vez)
crear_base_datos()
agregar_usuario("Matias Chacon", "clave123")
agregar_usuario("Arnold Rivera", "clave123")

# Web App con Flask
app = Flask(__name__)

html_form = """
    <h2>Login de usuarios</h2>
    <form method="POST">
        Nombre: <input type="text" name="nombre"><br>
        Clave: <input type="password" name="clave"><br>
        <input type="submit" value="Ingresar">
    </form>
    {% if mensaje %}
        <p>{{ mensaje }}</p>
    {% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def login():
    mensaje = ""
    if request.method == "POST":
        nombre = request.form["nombre"]
        clave = request.form["clave"]
        if validar_usuario(nombre, clave):
            mensaje = "Ingreso exitoso"
        else:
            mensaje = "Nombre o clave incorrecta"
    return render_template_string(html_form, mensaje=mensaje)

if __name__ == "__main__":
    app.run(port=7500)

from flask import Flask, jsonify

app = Flask(__name__)

# 1. Ruta Principal (texto plano / HTML)
@app.route("/")
def home():
    return """
    <h1>¡Bienvenido a mi App de Flask mejorada! 💡</h1>
    <p>Prueba visitar estas otras páginas en tu navegador:</p>

    <ul>
        <li><a href="/saludo/TuNombre">/saludo/TuNombre</a> (Ruta dinámica)</li>
        <li><a href="/api/info">/api/info</a> (Respuesta en formato JSON)</li>
    </ul>
    """

# 2. Ruta Dinámica (Captura una variable directamente desde la URL)
@app.route("/saludo/<nombre>")
def saludar(nombre):
    # El valor que pongas en la URL después de /saludo/ se guardará en la variable 'nombre'
    return f"<h2>¡Hola, {nombre}! Qué bueno verte por aquí. 👋</h2>"


# 3. Ruta de API (Devuelve datos en formato JSON, ideal para aplicaciones móviles o frontend)
@app.route("/api/info")
def api_info():
    datos = {
        "framework": "Flask",
        "lenguaje": "Python",
        "version_proyecto": "1.1",
        "estado": "Aprendiendo activamente",
        "herramientas": ["VS Code", "Virtualenv", "Pip"]
    }

    return jsonify(datos)  # Convierte el diccionario de Python a un JSON real


if __name__ == "__main__":
    app.run(debug=True)
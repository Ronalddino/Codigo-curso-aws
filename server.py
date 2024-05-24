from flask import render_template, Flask, request
import bd 

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')
    # Si no se pudieron obtener resultados, renderiza una plantilla con un mensaje de error

    
@app.route('/register_user')
def register_page():
    documento = request.args.get('documento')
    nombres = request.args.get('nombres')
    apellidos = request.args.get('apellidos')
    correo = request.args.get('correo')
    edad = request.args.get('edad')
    
    conexion = bd.conectar()
    
    if conexion:
        if documento and nombres and apellidos and correo and edad:
            resultados = bd.insertar(conexion, documento, nombres, apellidos, correo, edad)
        conexion.close()  # Cierra la conexión después de la consulta
        return render_template('register_user.html')
    else:
        return render_template('register_user.html', resultados=[])

    return render_template('register_user.html')

@app.route('/search_user', methods=['GET'])
def search_page():
    documento = request.args.get('documento')

    conexion = bd.conectar()
    if conexion:
        if documento:
            resultados = bd.consultar_por_documento(conexion, documento)
        else:
            resultados = bd.consultar(conexion)
        conexion.close()  # Cierra la conexión después de la consulta
        return render_template('search_user.html', resultados=resultados)
    else:
        return render_template('search_user.html', resultados=[])

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8080
    app.run(host, port, debug=True)
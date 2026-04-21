from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    data = request.get_json()
    estado = data.get('estado')

    if estado == 'on':
        return "OK: Encendido"
    elif estado == 'off':
        return "OK: Apagado"

    return "Acción no válida"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
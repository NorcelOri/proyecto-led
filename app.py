from flask import Flask, render_template, request

app = Flask(__name__)

estado_led = "off"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    global estado_led

    data = request.get_json()
    estado_led = data['estado']

    print("Estado:", estado_led)

    return f"LED {estado_led}"

@app.route('/estado')
def estado():
    return estado_led

if __name__ == '__main__':
    app.run(debug=True)
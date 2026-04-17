from flask import Flask, render_template
import serial

app = Flask(__name__)

arduino = serial.Serial('COM6', 9600)

@app.route('/')
def home():
    return '''
    <h1>Control LED</h1>
    <button onclick="fetch('/on')">Prender</button>
    <button onclick="fetch('/off')">Apagar</button>
    '''

@app.route('/on')
def encender():
    arduino.write(b'1')
    return "LED ON"

@app.route('/off')
def apagar():
    arduino.write(b'0')
    return "LED OFF"

app.run(host='0.0.0.0', port=5000)
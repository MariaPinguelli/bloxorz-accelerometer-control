from flask import Flask, render_template, request
from flask_socketio import SocketIO
import ssl
import pyautogui
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
socketio = SocketIO(app, cors_allowed_origins="*")

# Configurações
KEY_DELAY = 0.3  # Delay entre teclas
THRESHOLD = 0.8  # Sensibilidade ajustada

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print(f'Cliente conectado: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    print(f'Cliente desconectado: {request.sid}')

@socketio.on('accel_data')
def handle_accel_data(data):
    x, y = data.get('x', 0), data.get('y', 0)
    print(f"X: {x}, Y: {y}")
    
    # Lógica de direção com thresholds absolutos
    if abs(x) > THRESHOLD:
        direction = 'right' if x < 0 else 'left'
        press_key(direction)
    elif abs(y) > THRESHOLD:
        direction = 'down' if y < 0 else 'up'  # Invertido para orientação natural
        press_key(direction)

def press_key(direction):
    """Simula pressionamento de tecla com feedback visual"""
    print(f"Tecla pressionada: {direction}")
    # pyautogui.keyDown(direction)
    time.sleep(KEY_DELAY)
    # pyautogui.keyUp(direction)

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem')
    
    print("Servidor HTTPS rodando em https://0.0.0.0:5000")
    socketio.run(app, host='0.0.0.0', port=5000, ssl_context=context, debug=True)
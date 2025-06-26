from flask import Flask, render_template, request
from flask_socketio import SocketIO
import ssl
from pynput.keyboard import Controller, Key
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Configurações
KEY_DELAY = 0.1  # Delay entre teclas
THRESHOLD = 3.0  # Sensibilidade dos movimentos
NEUTRAL_THRESHOLD = 1.5  # Threshold para considerar como neutro
COOLDOWN = 0.5  # Tempo de espera após movimento
keyboard = Controller()

# Estado das teclas
last_key = None
last_movement_time = 0

KEY_MAPPING = {
    'up': Key.up,
    'down': Key.down,
    'left': Key.left,
    'right': Key.right
}

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
    global last_key, last_movement_time
    
    x, y = data.get('x', 0), data.get('y', 0)
    current_time = time.time()
    
    if current_time - last_movement_time < COOLDOWN:
        return
    
    is_neutral = abs(x) < NEUTRAL_THRESHOLD and abs(y) < NEUTRAL_THRESHOLD
    
    if last_key and is_neutral:
        last_key = None
        return
    
    if not is_neutral and last_key is None:
        if abs(x) > THRESHOLD:
            direction = 'right' if x < 0 else 'left'
            last_key = direction
            press_key(direction)
            last_movement_time = current_time
        elif abs(y) > THRESHOLD:
            direction = 'down' if y > 0 else 'up'
            last_key = direction
            press_key(direction)
            last_movement_time = current_time

def press_key(direction):
    """Simula pressionamento de tecla com feedback visual"""
    print(f"Tecla pressionada: {direction}")

    if direction in KEY_MAPPING:
        try:
            key = KEY_MAPPING[direction]
            keyboard.press(key)
            time.sleep(KEY_DELAY)
            keyboard.release(key)
        except Exception as e:
            print(f"Erro ao pressionar tecla: {e}")
    else:
        print(f"Direção inválida: {direction}")

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem')
    
    print("Servidor HTTPS rodando em https://0.0.0.0:5000")
    socketio.run(app, host='0.0.0.0', port=5000, ssl_context=context, debug=True)
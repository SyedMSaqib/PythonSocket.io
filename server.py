from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit
import base64

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@socketio.on('chat message')
def handle_message(msg):
    print(msg)
    socketio.emit('chat message', msg)

@socketio.on('user joined')
def handle_user_joined(username):
    message = {'name': 'System', 'message': f'{username} has joined the chat'}
    socketio.emit('chat message', message)

@socketio.on('audio')
def handle_audio(blob_data):
    print('Audio received')
    
    encoded_audio = base64.b64encode(blob_data)
    encoded_audio_str = encoded_audio.decode('utf-8')
    emit('audio', encoded_audio_str, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, port=3000, allow_unsafe_werkzeug=True)

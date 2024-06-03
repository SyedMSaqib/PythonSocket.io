from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit

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
def handle_audio(data):
    socketio.emit('audio', data)


if __name__ == '__main__':
    socketio.run(app,  port=3000, allow_unsafe_werkzeug=True)
# ,host='192.168.10.12'
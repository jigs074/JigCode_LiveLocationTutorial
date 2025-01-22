from flask import Flask, render_template 
from flask_socketio import SocketIO, emit 
from flask_cors import CORS 

app = Flask(__name__)

CORS(app)

socketio = SocketIO(app, cors_allowed_origins = "")

@app.route('/')
def index(): 
    return render_template('index.html')


@socketio.on('location')

def handle_location(data):
    emit('update', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
    
    
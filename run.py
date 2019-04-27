from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '14f09cc8d04ba4089cf680ece195fad8acb9aaf791024ca25db156ab095fd8a4'
app.config['FLASK_DEBUG'] = 1
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)


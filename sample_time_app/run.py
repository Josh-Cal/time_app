from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello! Visit /time to get the current time.'

@app.route('/time')
def time():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Current time: {now}\n'

app.run(host='0.0.0.0',
        port=8080,
        debug=True)

from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def home():
    message = os.getenv('APP_MESSAGE', 'Missing APP_MESSAGE')
    return message


@app.route('/health')
def health():
    health_status = os.getenv('APP_HEALTH', 'Missing APP_HEALTH')
    return health_status


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

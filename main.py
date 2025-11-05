from flask import Flask, request
import os
from fizzbuzz import generate_fizzbuzz
from fibonacci import generate_fibonacci

app = Flask(__name__)


@app.route('/')
def home():
    message = os.getenv('APP_MESSAGE', 'Missing APP_MESSAGE')
    return message


@app.route('/health')
def health():
    health_status = os.getenv('APP_HEALTH', 'Missing APP_HEALTH')
    return health_status


@app.route('/fizzbuzz', methods=['GET', 'POST'])
def fizzbuzz():
    if request.method == 'POST':
        try:
            n = int(request.form['number'])
            results = generate_fizzbuzz(n)
            return '<br>'.join(results)
        except ValueError:
            return 'Please enter a valid number.'
    return '''
        <form method="post">
            Enter a number for FizzBuzz: <input type="text" name="number">
            <input type="submit" value="Submit">
        </form>
    '''


@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        try:
            n = int(request.form['number'])
            results = generate_fibonacci(n)
            return '<br>'.join(results)
        except ValueError:
            return 'Please enter a valid number.'
    return '''
        <form method="post">
            Enter how many Fibonacci numbers to generate: <input type="text" name="number">
            <input type="submit" value="Submit">
        </form>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

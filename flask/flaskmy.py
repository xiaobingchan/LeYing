# -*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/appmy')
def appmy():
    return 'appmy'

if __name__ == '__main__':
    app.run(debug=True)
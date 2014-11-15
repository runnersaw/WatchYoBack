''' 
2048 vs AI Flask app

author: Sawyer
'''

from flask import Flask
from flask import render_template, redirect, request, jsonify, url_for

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def begin():
	return "Hello, world"

@app.route('/', methods = ['GET'])
def begin():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')

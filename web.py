''' 
2048 vs AI Flask app

author: Sawyer
'''

from flask import Flask
from flask import render_template, redirect, request, jsonify, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def begin():
	searchword = request.args.get('username', '')
	request.post("http://api.justyo.co/yo/", data={'api_token': 'd1c5ad87-a91d-498f-89f1-f17c6b432b2b', 'username': 'SVAUGHAN'})

if __name__ == '__main__':
	app.run(host='0.0.0.0')

''' 
Yo Flask App

author: Sawyer
'''

from flask import Flask
from flask import render_template, redirect, request, jsonify, url_for

API_TOKEN = 'd1c5ad87-a91d-498f-89f1-f17c6b432b2b'

def checkCrime():
	pass


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def begin():
	searchword = request.args.get('username')
	location = request.args.get('location')
	splittedLocation = location.split(';')
    latitude = splittedLocation[0]
    longitude = splittedLocation[1]

	request.post("http://api.justyo.co/yo/", data={'api_token': API_TOKEN, 'username': searchword })

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5000)

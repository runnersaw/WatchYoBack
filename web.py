''' 
Yo Flask App

author: Sawyer
'''

from flask import Flask
from flask import render_template, redirect, request, jsonify, url_for
import requests

API_TOKEN = 'd1c5ad87-a91d-498f-89f1-f17c6b432b2b'

def checkCrime():
	pass


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def begin():
	searchword = request.args.get('username')
	location = request.args.get('location')
	crimes = [{"type":"murder", "date":"now"}, {"type":"robbery", "date":"yesterday"}]
	#crimes = get_crimes()
	return render_template('index.html', lat=lat, lon=lon, crimes=crimes)

@app.route('/safe', methods = ['POST', 'GET'])
def safe():
	return render_template('safe.html')

@app.route('/yo', methods = ['POST', 'GET'])
def yo():
	searchword = request.args.get('username')
	location = request.args.get('location')
	requests.post("http://api.justyo.co/yo/", data={'api_token': 'd1c5ad87-a91d-498f-89f1-f17c6b432b2b', 'username': 'svaughan', 'link':'facebook.com/?location=42.360091;-71.09415999999999' })

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5000)

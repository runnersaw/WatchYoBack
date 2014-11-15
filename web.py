''' 
Yo Flask App

author: Sawyer
'''

from flask import Flask
from flask import render_template, redirect, request, jsonify, url_for
import requests
import json
from crimemap_api import get_bbox

API_TOKEN = 'd1c5ad87-a91d-498f-89f1-f17c6b432b2b'

def checkCrime():
	pass

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def begin():
	print 'yo'
	searchword = request.args.get('username')
	location = request.args.get('location')
	print 'yo'


	lat = location.split(';')[0]
	lon = location.split(';')[1]
	print 'yo'

	bbox = get_bbox((lat, lon))
	print 'yo'

	r = requests.get('http://sanfrancisco.crimespotting.org/crime-data?format=json&count=20&bbox="{}"').format(bbox)
	print 'YO'
	print r
	x= r.json()
	print 'yo'

	# print json.dumps(x)

	print 'hi'
	data = json.loads(json.dumps(x))

	for feature in data["features"]:
		coordinates = feature['geometry']['coordinates']
		break

	print 'ho'
	lat, lon = coordinates

	return render_template('index.html', lat=lat, lon=lon)

@app.route('/safe', methods = ['POST', 'GET'])
def safe():
	return render_template('safe.html')

@app.route('/yo', methods = ['POST', 'GET'])
def yo():
	searchword = request.args.get('username')
	location = request.args.get('location')

	requests.post("http://api.justyo.co/yo/", data={'api_token': 'd1c5ad87-a91d-498f-89f1-f17c6b432b2b', 'username': 'svaughan', 'link':'facebook.com/?location={};{}'.format(lat,long) })

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5000)

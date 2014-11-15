''' 
Yo Flask App

author: Sawyer
'''

from flask import Flask
from flask import render_template, redirect, request, jsonify, url_for
import requests
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

	# lats = location.split(';')[0]
	# longs = location.split(';')[1]

	# bbox = get_bbox((lats, longs)

	# r = requests.get('http://sanfrancisco.crimespotting.org/crime-data?format=json&count=20&bbox={}'.format(bbox))
	# x= r.json()

	# # print json.dumps(x)

	# data = json.loads(json.dumps(x))

	# for feature in data["features"]:
	# 	coordinates = feature['geometry']['coordinates']
	# 	break

	crimes = [{"type":"murder", "date":"now"}, {"type":"robbery", "date":"yesterday"}]
	#crimes = get_crimes()
	# lat, lon = coordinates
	return render_template('index.html', lat=lat, lon=lon, crimes=crimes)

@app.route('/safe', methods = ['POST', 'GET'])
def safe():
	return render_template('safe.html')

@app.route('/yo', methods = ['POST', 'GET'])
def yo():
	searchword = request.args.get('username')
	location = request.args.get('location')


	lats = location.split(';')[0]
	longs = location.split(';')[1]

	bbox = get_bbox((lats, longs))

	r = requests.get('http://sanfrancisco.crimespotting.org/crime-data?format=json&count=20&bbox="{}"'.format(bbox))
	x= r.json()

	# print json.dumps(x)

	data = json.loads(json.dumps(x))

	for feature in data["features"]:
		coordinates = feature['geometry']['coordinates']
		break

	lat, lon = coordinates
	requests.post("http://api.justyo.co/yo/", data={'api_token': 'd1c5ad87-a91d-498f-89f1-f17c6b432b2b', 'username': 'svaughan', 'link':'facebook.com/?location={};{}'.format(lat,long) })

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5000)

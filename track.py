import json
import requests

if __name__ == '__main__':
	current_location

	r = requests.get('http://sanfrancisco.crimespotting.org/crime-data?format=json&count=20')
	x= r.json()

	# print json.dumps(x)

	data = json.loads(json.dumps(x))

	for feature in data["features"]:
		print feature['geometry']['coordinates']


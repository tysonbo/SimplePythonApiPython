import urllib.parse
import requests


api_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = input('Address: ')
	url = api_url + urllib.parse.urlencode({'address': address})
	print(url)
	json_response = requests.get(url).json()

	json_status = json_response['status']
	print('API Status: ' + json_status)
	print();

	if json_status == 'OK':
		for each in json_response['results'][0]['address_components']:

			print(each['long_name'])
		else:
  			print("There was an error please try again.")

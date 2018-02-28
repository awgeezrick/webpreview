import requests
import base64
import json


def _get_image(url, filename, type):

	valid_types = ["desktop", "mobile"]

	if type not in valid_types:
		return 'not valid type. must be "desktop" or "mobile"'

	API_URL = "https://www.googleapis.com/pagespeedonline/v1/runPagespeed?screenshot=true&strategy={}&url={}"
	request_url = API_URL.format(type, url)

	response = requests.get(request_url)

	try:
		data = response.json()

	except:
		return "unable to retreive data"

	try:
		screenshot_encoded =  data["screenshot"]["data"]
	except ValueError:
		return "invalid JSON encountered"
	
	screenshot_encoded = screenshot_encoded.replace("_", "/")
	screenshot_encoded = screenshot_encoded.replace("-", "+")

	screenshot_decoded = base64.b64decode(screenshot_encoded)


	with open(filename, 'wb') as f:
		f.write(screenshot_decoded)


def mobile(url, filename):
	_get_image(url, filename, type="mobile")


def desktop(url, filename):
	_get_image(url, filename, type="desktop")


import json
import urllib.request
import urllib.error


def get_google_result(query):
	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='
	url += '%20'.join(query)
	qs = '+'.join(query)
	search_url = 'https://www.google.com/?q='+qs+'#q='+qs

	result = urllib.request.urlopen(url)
	response = result.read().decode()
	result.close()
	data = json.loads(response)

	if data['responseData'] and data['responseData']['results']:
		result = data['responseData']['results'][0]
		result = result['title'] + ' - ' + result['unescapedUrl']
		return 'First result: ' + result + ' -- ' + search_url
	else:
		return 'No results!'

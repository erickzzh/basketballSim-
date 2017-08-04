# Install the Python Requests library:
# `pip install requests`

import base64
import requests


def send_request():
    # Request

    try:
        response = requests.get(
            url={pull-url},
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format({username},{password}).encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')






hey():
	pass        
	json_data=open(roster_2016_2017_directory).read()
	data=json.loads(json_data)
	#pprint(data)
	pprint(data['rosterplayers']['playerentry'])
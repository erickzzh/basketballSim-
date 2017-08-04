import base64
import requests
import urllib
import json
from pprint import pprint
usernmae=""
password=""

def send_request():
    # Request

    try:
        response = requests.get(
            url=URL,
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(usernmae,password).encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        
        pprint('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')



#placeholders
fileFormat = "json"
sesonNameBegin=input("Enter the beginning of the season ")+"-"
seasoNameEnd=input("Enter the end of the season ")+"-"
dataCat='cumulative_player_stats' #temp need to dynamically change the data type
#dataCat=input("Enter the data type that you want ")
seasonNameType=input("Enter either 'regular' or 'playoff '")
optionParam='?'+input("Enter optional parameters ")


#differentiate the two type of games 
if seasonNameType=="playoff":
    URL='https://www.mysportsfeeds.com/api/feed/pull/nba/{}{}/{}.{}'.format(sesonNameBegin,seasonNameType,dataCat,fileFormat)
else:
    URL='https://www.mysportsfeeds.com/api/feed/pull/nba/{}{}{}/{}.{}'.format(sesonNameBegin,seasoNameEnd,seasonNameType,dataCat,fileFormat)


#have the options to add different parameters according to different data type
#https://www.mysportsfeeds.com/data-feeds/api-docs/#
while(optionParam!='?0'):
    URL=URL+optionParam
    optionParam='?'+input("Enter optional parameters ")

print(URL)

send_request();

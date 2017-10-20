import requests # pip install requests
import json

# generate a token with your client id and client secret
token = requests.post('https://www.arcgis.com/sharing/rest/oauth2/token/', params={
  'f': 'json',
  'client_id': '4Q63Bzg2VyJK2Lay',
  'client_secret': '16af622a202a433b845f9fd5f06c220c',
  'grant_type': 'client_credentials',
  'expiration': '1440'
})



routesURL = 'http://route.arcgis.com/arcgis/rest/services/World/Route/NAServer/Route_World/solve'
token = token.json()['access_token']
stops = '-122.4079,37.78356;-122.404,37.782'
format = 'json'

requestURL = routesURL + '?token=' + token + '&stops=' + stops + '&f=' + format

data = requests.get(requestURL)

print json.dumps(data.json(), indent=4, sort_keys=True)
import os

import requests

app_id = os.environ['YELP_CONSUMER_KEY']
app_secret = os.environ['YELP_CONSUMER_SECRET']

data = {'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': app_secret}
token = requests.post('https://api.yelp.com/oauth2/token', data=data)
access_token = token.json()['access_token']
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'bearer %s' % access_token}
params = {'location': 'San Fran',
          'term': 'Chinese Restaurant',
          'sort_by': 'rating'
          }

resp = requests.get(url=url, params=params, headers=headers)

import pprint
pprint.pprint(resp.json()['businesses'])

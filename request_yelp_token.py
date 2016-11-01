import requests

app_id = 'client_id'
app_secret = 'client_secret'
data = {'grant_type': 'client_credentials',
        'client_id': 'jljTSp0dnGWWTPeU53ymow',
        'client_secret': 'wo3XQku6AF1NS1vGDXixRkl4f23FRy4J5aSqe8CcI4p6hitGJMoqmwrJBn71t5yP'}
token = requests.post('https://api.yelp.com/oauth2/token', data=data)
access_token = token.json()

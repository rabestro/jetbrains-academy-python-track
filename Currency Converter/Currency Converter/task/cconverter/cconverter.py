import requests
import json

code = input().lower()
url = f'http://www.floatrates.com/daily/{code}.json'
response = requests.get(url)
data = json.loads(response.text)
print(data['usd'])
print(data['eur'])

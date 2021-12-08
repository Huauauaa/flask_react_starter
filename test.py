from requests import get

BASE_URL = 'http://localhost:5000'
response = get(BASE_URL + '/video/1')

print(response.json())

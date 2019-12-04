import requests
import json

# url = 'http://0.0.0.0:5000/api/'
url = 'http://localhost:5000/api/'

data = [[0.58777537, -1.28362673,  0.73608136,  0.94067266]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)
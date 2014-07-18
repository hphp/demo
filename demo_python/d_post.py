import requests
import json

headers = {'content-type': 'application/json'}
url = "http://localhost/cgi-bin/demo_get_PostRawData.py"

data = {"h":"hh", "hhh":3}
result = requests.post(url, data=json.dumps(data), headers=headers)
print result
print result.status_code
print result.text

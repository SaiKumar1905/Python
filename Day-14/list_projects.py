# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://saikumarthondala1905.atlassian.net//rest/api/3/project"
api_Token=""
auth = HTTPBasicAuth("saikumarthondala1905@gmail.com", api_Token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output=json.loads(response.text)
print(output[0]["name"])

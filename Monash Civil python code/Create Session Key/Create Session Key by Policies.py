import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class WebServices(object):

    def __init__(self, host_url="", session=None):
        self.host_url = host_url
        self.session = session if session != None else requests.Session()

    def set_api_key(self, api_key):
        self.headers = {'x-ni-api-key':api_key, 'Content-Type':'application/json'}
        self.auth = ""
        
    def post_route(self, url, post_json):
        print("POST " + self.host_url + url)
        response = self.session.post(self.host_url+url, json=post_json, verify=False, headers=self.headers, auth=self.auth)
        print(str(response))
        return response
    
# Manually set the connection credentials for whitelisted routes
host_url = "http://localhost:12100/" # must bypass SystemLink Web Server (443), which refuses whitelisted requests
api_key = "7FEWVlmRpr-VhK_Pr237B1rDqp6HuaLsFIMd2NdSzn" # must use whitelisted ApiKey

# Return WebServiceRoutes object
webServices = WebServices(host_url)

# Define the connection credentials in the response header using the whitelisted ApiKey
webServices.set_api_key(api_key)

# Define the new Seesion Key
session_key_json = {
  "orgId": "891c595f-9121-45e1-8515-9d54783393f3",
  "userId": "b8482a4a-3ef6-4e37-8975-d6aad135dbb5",
  "policyIds": ["94bdeb16-eeb9-42fd-bef0-12b963b36b46","8f1be054-e0c7-4699-af74-bade4a203c57","a256bd29-12ec-4cb0-b59e-19c03c47f3c6","7d80bb61-8df6-499c-b1e4-3d89848f8633"],
  "durationSeconds": 120,
  "properties": {"temp": "yes"}
}

# Run Web Service Route to create Session Key
response = webServices.post_route("niauth/v1/session-keys", session_key_json)
print(str(response.json()))
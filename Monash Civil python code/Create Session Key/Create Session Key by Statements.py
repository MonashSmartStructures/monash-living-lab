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

# Define the new session key
session_key_json = {
  "orgId": "891c595f-9121-45e1-8515-9d54783393f3",
  "userId": "b8482a4a-3ef6-4e37-8975-d6aad135dbb5",
  "policies": [
    {
      "statements": [
        {
          "actions": [
            "file:Query",
            "file:Download",
            "file:Upload",
            "file:Update"
          ],
          "description": "File Maintainer",
          "resource": ["*"],
          "workspace": "*"
        },
        {
          "actions": [
            "tag:QueryTagMetadata",
            "tag:QueryTagValue",
            "taghistory:Read",
            "tag:CreateTagMetadata",
            "taghistory:Create",
            "tag:UpdateTagValue",
            "tag:UpdateTagMetadata",
            "tag:DeleteTagMetadata"
          ],
          "description": "Tag Automated Agent",
          "resource": ["*"],
          "workspace": "*"
        }
      ]
    }
  ],
  "durationSeconds": 120,
  "properties": {"temp": "yes"}
}

# Run Web Service Route to create Session Key
response = webServices.post_route("niauth/v1/session-keys", session_key_json)
print(str(response.json()))
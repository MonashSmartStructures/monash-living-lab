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
        
    def set_usr_pwd(self, username, password):
        self.headers = ""
        self.auth = (username, password)
    
    def post_route(self, url, post_json):
        print("POST " + self.host_url + url)
        response = self.session.post(self.host_url+url, json=post_json, verify=False, headers=self.headers, auth=self.auth)
        print(str(response))
        return response
    
# Connection Info
host_url = "https://localhost:443/"
api_key = "AU2hWR8LfzeeszVg1R0ZviS_tlwmf8XjQF3JFGUkrG" # Run os.getenv("SYSTEMLINK_API_KEY") in JupyterHub to get ApiKey

# Return WebServiceRoutes object
webServices = WebServices(host_url)

# Define the connection credentials in the response header using an ApiKey or username/password
#webServices.set_api_key(api_key)
webServices.set_usr_pwd("admin", "mypassword")

# Define the new API Key
api_key_json = {
  "name": "Super User Access Script",
  "policyIds": ["7d80bb61-8df6-499c-b1e4-3d89848f8633"],
  "properties": {"ApiKeyType": "programmatic"}
} #   "defaultWorkspace": "Default"

# Run Web Service Route to create API Key
response = webServices.post_route("niauth/v1/keys", api_key_json)
print(str(response.json()))

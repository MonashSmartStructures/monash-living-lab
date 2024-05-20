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
        
    def get_route(self, url):
        print("GET " + self.host_url + url)
        response = self.session.get(self.host_url+url, json={}, verify=False, headers=self.headers, auth=self.auth)
        print(str(response))
        return response
    
    def post_route(self, url, post_json):
        print("POST " + self.host_url + url)
        response = self.session.post(self.host_url+url, json=post_json, verify=False, headers=self.headers, auth=self.auth)
        print(str(response))
        return response

    def put_route(self, url, put_json):
        print("PUT " + self.host_url + url)
        response = self.session.put(self.host_url+url, json=put_json, verify=False, headers=self.headers, auth=self.auth)
        print(str(response))
        return response
    
    def patch_route(self, url, patch_json):
        print("PATCH " + self.host_url + url)
        response = self.session.patch(self.host_url+url, json=patch_json, verify=False, headers=self.headers, auth=self.auth)
        print(str(response))
        return response

    def delete_route(self, url, delete_json):
        print("DELETE " + self.host_url + url)
        response = self.session.delete(self.host_url+url, json=delete_json, verify=False, headers=self.headers, auth=self.auth)
        print(str(response))
        return response

# Authentication Parameters
host_url = "https://demo.systemlink.io/"
#host_url = "https://test.systemlink.io/"
username = "lvadmin"
password = "LabVIEW==="

# Return WebServices object (set host_url)
webServices = WebServices(host_url)

# Define the connection credentials in the response header using an ApiKey or username/password
#webServices.set_api_key(api_key)
webServices.set_usr_pwd(username, password)

# Run Web Service Route to return tag count
response = webServices.get_route("nitag/v2/tags-count")
#response = webServices.get_route("niuser/v1/workspaces")
print(str(response.json()))

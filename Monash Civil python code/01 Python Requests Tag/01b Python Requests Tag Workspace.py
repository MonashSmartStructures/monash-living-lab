import requests
import urllib3
from datetime import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class WebServices(object):

    def __init__(self, host_url="", session=None):
        self.host_url = host_url
        self.session = session if session != None else requests.Session()

    def set_api_key(self, api_key):
        self.headers = {'x-ni-api-key':api_key}
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


def write_tag(webServices, tag_path, tag_properties, tag_value, tag_workspace):
    tag = {'collect_aggregates': False, 'keywords': None, 'path': tag_path, 'properties': tag_properties, 'type': 'STRING', 'workspace': tag_workspace}
    response = webServices.post_route("nitag/v2/tags", tag)
    if tag_workspace != None and tag_workspace != "":
        response = webServices.put_route("nitag/v2/tags/"+tag_workspace+"/"+tag_path+"/values/current", tag_value)
    else:
        response = webServices.put_route("nitag/v2/tags/"+tag_path+"/values/current", tag_value)


def read_tag(webServices, tag_path, tag_workspace):
    if tag_workspace != None and tag_workspace != "":
        response = webServices.get_route("nitag/v2/tags/"+tag_workspace+"/"+tag_path+"/values")
    else:
        response = webServices.get_route("nitag/v2/tags/"+tag_path+"/values")
    tag = response.json()
    return tag


def tag_io(webServices):
    now = datetime.today().isoformat() # "2019-09-05T18:45:08Z"
    tag_path = "NI_PXIe-8133_Embedded_Controller--MAC-00-80-2F-12-7F-31.Ownership.Status"
    tag_properties = {"IsConformed": "true", "Department": "OPS", "IsReleased": "true"}
    tag_value = {"value": {"type": "STRING", "value": "OPS"}, "timestamp": now}
    tag_workspace = None # workspace = Default
    tag_workspace = "93f869bd-f4df-4fb6-84e3-0499cae06a7c" # workspace != Default
    write_tag(webServices, tag_path, tag_properties, tag_value, tag_workspace)
    tag = read_tag(webServices, tag_path, tag_workspace)
    print(str(tag))


# Connection Info
host_url = "https://localhost:443/"
api_key = "wSo_Orl4sRY5a0n922pDjsFp6kPlKFhl2kdFFQQ5Gz" # Run os.getenv("SYSTEMLINK_API_KEY") in JupyterHub to get your ApiKey

# Return WebServices object (set host_url)
webServices = WebServices(host_url)

# Define the connection credentials using an ApiKey or username/password
#webServices.set_api_key(api_key)
webServices.set_usr_pwd("admin", "mypassword")

# perform tag operations
tag_io(webServices)
print("done")
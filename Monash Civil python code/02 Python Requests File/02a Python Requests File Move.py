import os
import requests
import urllib3
import logging
import http.client as http_client
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
    
    def post_route(self, url, post_json="", post_files=""):
        print("POST " + self.host_url + url)
        response = self.session.post(self.host_url+url, json=post_json, files=post_files, verify=False, headers=self.headers, auth=self.auth)
        print(str(response))
        return response

    def put_route(self, url, put_json):
        print("PUT " + self.host_url + url)
        response = self.session.put(self.host_url+url, json=put_json, verify=False, headers=self.headers, auth=self.auth)
        print(str(response))
        return response


def make_local_file(file_name, file_content):
    current_script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = current_script_dir + "\\" + file_name
    f = open(file_path, "w", encoding="utf-8")
    f.write(file_content)
    f.close()
    print(str('Created "' + file_name + '" ==> ' + file_content))
    return file_path


def upload_file(webServices, file_path, file_name):
    f = open(file_path, 'r')
    file_content = f.read()
    f.close()
    files = {'file': (file_name, file_content)}
    response = webServices.post_route("nifile/v1/service-groups/Default/upload-files", post_files=files)
    response_json = response.json()
    print(str(response_json))
    file_id = str(response_json['uri'])[-24:]
    return file_id


def download_file(webServices, file_id):
    response = webServices.get_route("nifile/v1/service-groups/Default/files/" + file_id + "/data?inline=false")
    response_body = response.content
    file_body = str(response_body.decode()).replace("\r", "")
    return file_body


def file_io(webServices): # assumes you are ONLY using the Default workspace
    file_name = "Example File.csv"
    now = datetime.today().isoformat() # "2019-09-05T18:45:08Z"
    file_path = make_local_file(file_name, str(now))
    print(file_path)
    file_id = upload_file(webServices, file_path, file_name)
    print(file_id)
    file = download_file(webServices, file_id)
    print(str(file))
    return file_id


# Connection Info
host_url = "https://localhost:443/"
api_key = "wSo_Orl4sRY5a0n922pDjsFp6kPlKFhl2kdFFQQ5Gz"  # Run os.getenv("SYSTEMLINK_API_KEY") in JupyterHub to get your ApiKey
#api_key = "lzXD0gsb6YLTlxJDk7a_YwkSigMUDIW1fADx_Myl8h" # cached at "C:\ProgramData\National Instruments\Skyline\HttpConfigurations\"

# Return WebServices object (set host_url)
webServices = WebServices(host_url)

# Define the connection credentials using an ApiKey or username/password
#webServices.set_api_key(api_key)
webServices.set_usr_pwd("admin", "mypassword")

# perform tag operations
file_io(webServices)
print("done")
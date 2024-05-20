import requests
import urllib3
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
        route = "GET " + str(self.host_url) + str(url)
        response = self.session.get(self.host_url+url, json={}, verify=False, headers=self.headers, auth=self.auth)
        print(str(response) + " , " + route)
        return response
    
    def post_route(self, url, post_json):
        route = "GET " + str(self.host_url) + str(url)
        response = self.session.post(self.host_url+url, json=post_json, verify=False, headers=self.headers, auth=self.auth)
        print(str(response) + " , " + route)
        return response


def service_status_output(output, down_count, service_name, response):
    if output != "": output = output + "\r\n"
    output = output + str(response) + " , " + str(service_name)
    if str(response) != "<Response [200]>": down_count = down_count + 1
    return output, down_count


# Authentication Parameters
host_url = "https://localhost:443/"
api_key = "sFdl7LvftsSWimicQ_yCWBUa5cuHwTXoFwrq-oTfBF"

# Return WebServices object (set host_url)
webServices = WebServices(host_url)

# Define the connection credentials in the response header using an ApiKey or username/password
#webServices.set_api_key(api_key)
webServices.set_usr_pwd("admin", "mypassword")

# Run Web Service Route to return output and down_count
output = ""
down_count = 0
output, down_count = service_status_output(output, down_count, "Alarms", webServices.get_route("nialarm"))
output, down_count = service_status_output(output, down_count, "Analysis Server", webServices.get_route("TDMServer_as/ping"))
output, down_count = service_status_output(output, down_count, "Analysis Procedure Packaging", webServices.get_route("niaspkg"))
output, down_count = service_status_output(output, down_count, "Asset Performance", webServices.get_route("niapm"))
output, down_count = service_status_output(output, down_count, "Asset Performance Rules", webServices.get_route("niapmrule"))
output, down_count = service_status_output(output, down_count, "Authentication", webServices.get_route("niauth/v1/auth"))
output, down_count = service_status_output(output, down_count, "Data Analysis", webServices.get_route("nidataanalyzer"))
output, down_count = service_status_output(output, down_count, "Data Cart", webServices.get_route("nidatacart"))
output, down_count = service_status_output(output, down_count, "Data Navigator", webServices.get_route("ni/asam/about"))
output, down_count = service_status_output(output, down_count, "Data Naming", webServices.get_route("ni/asam/ni/nameservice/ods/url"))
output, down_count = service_status_output(output, down_count, "Data Navigator Utils", webServices.get_route("DataNavigator/ping"))
output, down_count = service_status_output(output, down_count, "Data Preprocessor", webServices.get_route("TDMServer_dprepro/ping"))
output, down_count = service_status_output(output, down_count, "Data Indexing", webServices.get_route("TDMServer_dfse/ping"))
output, down_count = service_status_output(output, down_count, "DataPlugins", webServices.get_route("nidatapluginmanager/v1/about"))
output, down_count = service_status_output(output, down_count, "Data Federation", webServices.get_route("TDMServer_fed/ping"))
output, down_count = service_status_output(output, down_count, "Files", webServices.get_route("nifile"))
output, down_count = service_status_output(output, down_count, "Messages", webServices.post_route("nimessage/v1/sessions", {}))
output, down_count = service_status_output(output, down_count, "Notebook Execution", webServices.get_route("ninbexec"))
output, down_count = service_status_output(output, down_count, "OPC Client", webServices.get_route("niopcclient"))
output, down_count = service_status_output(output, down_count, "Package Repository", webServices.get_route("nirepo/v1/ping"))
output, down_count = service_status_output(output, down_count, "TDM Server", webServices.get_route("TDMServer/ping"))
output, down_count = service_status_output(output, down_count, "Systems Management", webServices.get_route("nisysmgmt"))
output, down_count = service_status_output(output, down_count, "Systems State", webServices.get_route("nisystemsstate"))
output, down_count = service_status_output(output, down_count, "Tag Historian", webServices.get_route("nitaghistorian"))
output, down_count = service_status_output(output, down_count, "Tag Rule Engine", webServices.get_route("nitagrule"))
output, down_count = service_status_output(output, down_count, "Tags", webServices.get_route("nitag"))
output, down_count = service_status_output(output, down_count, "TDM Reader", webServices.get_route("nitdmreader"))
output, down_count = service_status_output(output, down_count, "Test Monitor", webServices.get_route("nitestmonitor"))
output, down_count = service_status_output(output, down_count, "User Data", webServices.get_route("niuserdata"))
output, down_count = service_status_output(output, down_count, "Users", webServices.post_route("niuser/v1/users/query", {"filter": "firstName.StartsWith(\"Z123\")"}))
print(output)
print(str(down_count))


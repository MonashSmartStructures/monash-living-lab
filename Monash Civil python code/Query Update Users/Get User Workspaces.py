from WebServices import WebServices


def GetUser(user_id):
    url = "niuser/v1/users/" + str(user_id)
    user = webServices.get_route(url)
    user_dict = user.json()
    return user_dict


def GetPolicy(policy_id):
    url = "niauth/v1/policies?id=" + str(policy_id)
    policy = webServices.get_route(url)
    policy_dict = policy.json()
    return policy_dict


# Connection Info
host_url = "https://localhost:443/"
api_key = "_Vtq8Ez72mgzmL6xdDnlmsyB_OvZGuXXUP-m5tfvei"
api_key = "NmCT3Lnh84QfQW2NAPJQuUzC5N6SPYrVOtobQdjHOv" # "C:\ProgramData\National Instruments\Skyline\HttpConfigurations\http_master.json"
#api_key = "AU2hWR8LfzeeszVg1R0ZviS_tlwmf8XjQF3JFGUkrG" # Run os.getenv("SYSTEMLINK_API_KEY") in JupyterHub to get ApiKey

# Return WebServices object (set host_url)
webServices = WebServices(host_url)

# Define the connection credentials using an ApiKey or username/password
webServices.set_api_key(api_key)
#webServices.set_usr_pwd("admin", "mypassword")

# Get Policies from User and read Workspace_IDs
user_id = "a3ffc5d9-fe77-4535-bfee-28ce2eb0d8dc"
#user_id = "b8482a4a-3ef6-4e37-8975-d6aad135dbb5"
user_dict = GetUser(user_id)
print(str(user))
policies = user_dict['policies']
#policies = []
for policy_id in policies:
    policy_dict = GetPolicy(policy_id)
    policy = policy_dict['policies'][0]
    built_in = policy['builtIn']
    if built_in != True:
        workspace_id = policy['workspace']
        print(str(policy_id) + " ==> " + str(workspace_id))

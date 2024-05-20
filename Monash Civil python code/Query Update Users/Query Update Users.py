from WebServices import WebServices

def QueryUsers():
    # Query Parameters
    query_json = {'filter': 'id="b8482a4a-3ef6-4e37-8975-d6aad135dbb5"'}
    query_json = {}
    # Query Users
    users = webServices.post_route("niuser/v1/users/query", query_json)
    user_dict = users.json()
    return user_dict["users"]

def UpdateFirstNames(users):
    for user in users:
        user_id = user["id"]
        first_name = user["firstName"]
        if first_name[0:3] == "aaa":
            first_name = first_name[3:]
        else:
            first_name = "aaa" + first_name
        update_json = {"firstName": first_name}
        print("-------------------------------------------------------------------------")
        print("updating user " + user_id + " to firstName = " + first_name)
        response = webServices.put_route("niuser/v1/users/"+user_id, update_json)

# Connection Info
host_url = "https://localhost:443/"
api_key = "AU2hWR8LfzeeszVg1R0ZviS_tlwmf8XjQF3JFGUkrG" # Run os.getenv("SYSTEMLINK_API_KEY") in JupyterHub to get ApiKey

# Return WebServices object (set host_url)
webServices = WebServices(host_url)

# Define the connection credentials using an ApiKey or username/password
#webServices.set_api_key(api_key)
webServices.set_usr_pwd("admin", "mypassword")

# Query and Update Users
users = QueryUsers()
print(str(users))
UpdateFirstNames(users)


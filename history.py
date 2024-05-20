import os
import urllib3
import logging
import http.client as http_client
from datetime import datetime
from webservice import WebServices
from configuration import configuration,username,password
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def make_local_file(file_name, file_content):
    current_script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = current_script_dir + "\\" + file_name
    f = open(file_path, "w", encoding="utf-8")
    f.write(file_content)
    f.close()
    print(str('Created "' + file_name + '" ==> ' + file_content))
    return file_path


def upload_file(webServices, file_path, file_name, workspace):
    f = open(file_path, 'r')
    file_content = f.read()
    f.close()
    files = {'file': (file_name, file_content)}
    if workspace != None and workspace != "":
        response = webServices.post_route("nifile/v1/service-groups/Default/upload-files?workspace=" + workspace,
                                          post_files=files)
    else:  # Default workspace
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


def file_io(webServices):  # assumes you are ONLY using the Default workspace
    workspace = None  # Default workspace
    # workspace = "93f869bd-f4df-4fb6-84e3-0499cae06a7c" # workspace != Default , workspace = foo
    file_name = "202405201430_SHM-7.tdms"
    now = datetime.today().isoformat()  # "2019-09-05T18:45:08Z"
    file_path = make_local_file(file_name, str(now))
    file_id = "202405201430_SHM-7.tdms"
    print(file_path)
    #file_id = upload_file(webServices, file_path, file_name, workspace)
    #print(file_id)
    file = download_file(webServices, file_id)
    print(str(file))
    return file_id


if __name__ == '__main__':
    # Connection Info
    host_url = "https://woodside-shm.eng.monash.edu/"
    api_key = "wSo_Orl4sRY5a0n922pDjsFp6kPlKFhl2kdFFQQ5Gz"  # Run os.getenv("SYSTEMLINK_API_KEY") in JupyterHub to get your ApiKey
    # api_key = "lzXD0gsb6YLTlxJDk7a_YwkSigMUDIW1fADx_Myl8h" # cached at "C:\ProgramData\National Instruments\Skyline\HttpConfigurations\"

    # Return WebServices object (set host_url)
    webServices = WebServices(host_url)

    # Define the connection credentials using an ApiKey or username/password
    # webServices.set_api_key(api_key)
    webServices.set_usr_pwd(username, password)

    # perform tag operations
    file_io(webServices)
    print("done")

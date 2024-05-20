import requests


class WebServices(object):

    def __init__(self, host_url="", session=None):
        self.host_url = host_url
        self.session = session if session != None else requests.Session()

    def set_api_key(self, api_key):
        self.headers = {'x-ni-api-key': api_key}
        self.auth = ""

    def set_usr_pwd(self, username, password):
        self.headers = ""
        self.auth = (username, password)

    def get_route(self, url):
        print("GET " + self.host_url + url)
        response = self.session.get(self.host_url + url, json={}, verify=False, headers=self.headers, auth=self.auth)
        print(str(response))
        return response

    def post_route(self, url, post_json="", post_files=""):
        print("POST " + self.host_url + url)
        response = self.session.post(self.host_url + url, json=post_json, files=post_files, verify=False,
                                     headers=self.headers, auth=self.auth)
        print(str(response))
        return response

    def put_route(self, url, put_json):
        print("PUT " + self.host_url + url)
        response = self.session.put(self.host_url + url, json=put_json, verify=False, headers=self.headers,
                                    auth=self.auth)
        print(str(response))
        return response

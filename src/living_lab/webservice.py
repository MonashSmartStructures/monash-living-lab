import requests


class WebServices(object):
    """Class to create web service request"""
    def __init__(self, host_url="", session=None):
        self.host_url = host_url
        self.session = session if session != None else requests.Session()

    def set_api_key(self, api_key):
        """Sets the API key

        Parameters
        ----------
        api_key: str
            API key

        """
        self.headers = {'x-ni-api-key': api_key}
        self.auth = ""

    def set_usr_pwd(self, username, password):
        """Sets the username and password

        Parameters
        ----------
        username: str
        password: str

        """
        self.headers = ""
        self.auth = (username, password)

    def get_route(self, url):
        """Get command of request

        Parameter
        ---------
        url: str
            The HTTP api url for get command
        """
        print("GET " + self.host_url + url)
        response = self.session.get(self.host_url + url, json={}, verify=False, auth=self.auth)
        print(str(response))
        return response

    def post_route(self, url, post_json="", post_files=""):
        """
        Post command of request

        Parameter
        ---------
        url: str
            The HTTP api url for get command
        post_json: str, optional
            json file to post
        post_file: str, optional
            file to post
        """
        print("POST " + self.host_url + url)
        response = self.session.post(self.host_url + url, json=post_json, files=post_files, verify=False,
                                     headers=self.headers, auth=self.auth)
        print(str(response))
        return response

    def put_route(self, url, put_json):
        """
        Put command of request

        Parameter
        ---------
        url: str
            The HTTP api url for get command
        put_json: str, optional
            json file to put
        """
        print("PUT " + self.host_url + url)
        response = self.session.put(self.host_url + url, json=put_json, verify=False, headers=self.headers,
                                    auth=self.auth)
        print(str(response))
        return response

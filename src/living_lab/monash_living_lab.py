import urllib3
from webservice import WebServices
from tdms_reader import TDMS
import ast
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class MonashLivingLab:
    """API Wrapper for Monash Living Lab's NI Systemlink """

    def __init__(self, username:str, password:str):
        # init var
        self.data = None
        self.download_filename = None

        # create Living Lab webservice
        self.host_url = "https://woodside-shm.eng.monash.edu"
        self.webService = self.create_service(username, password)

        # get available tdms files
        available_file_url = "/nifile/v1/service-groups/Default/files?skip=0&take=0&orderBy=id&orderByDescending=false"
        query = self.webService.get_route(available_file_url)
        self.available_files = query.json()
        self.files = [file["properties"]["Name"] for file in self.available_files["availableFiles"]]
        self.file_id = [file["id"] for file in self.available_files["availableFiles"]]

        # get all available tags
        #available_tag =


        print("Connection established")

    def create_service(self, usn:str, pw:str):
        # Create the webService object
        webServices = WebServices(self.host_url)
        webServices.set_usr_pwd(usn, pw)

        return webServices

    def get_tag_values(self, tagname:str):
        """Returns the tag history values

        Parameter
        ---------
        tagname: str
            Name of the tag

        """

        url = "/nitag/v2/tags-with-values/{path}".format(path=tagname)
        response = self.webService.get_route(url) # byte object
        return json.loads(response.content.decode('utf-8'))

    def get_tag_history(self, request_body=None):
        """Returns the tag history between a given start and end time

        Parameter
        ---------
        request_body: dict
            The request body - see below for example of request body

        Examples
        --------
        {
            "path": "system1.tag1",
            "workspace": "0c80cf49-54e9-4e92-b117-3bfa574caa84",
            "startTime": "2018-09-04T18:45:08Z",
            "endTime": "2018-09-04T18:45:08Z",
            "take": 1,
            "continuationToken": "string",
            "sortOrder": "ASCENDING"
            }

        Returns
        -------
        ValueError if
        """

        if request_body is None:
            request_body = ""
        url = "/nitaghistorian/v2/tags/query-history"

        history = self.webService.post_route(url=url,post_json=request_body)

        return json.loads(history.content.decode('utf-8'))


    def get_tdms_file(self, filename):
        """Download tdms file

        Parameter
        ---------
        filename:str
            Name of tdms file
        """
        self.download_filename = filename
        if ".tdms" not in filename:
            raise ValueError("file name needs to be a filename with .tdms extension")

        # index file
        i = [i for i, x in enumerate(self.files) if x == self.download_filename]
        if not i:  # empty list
            raise Exception("File does not exist")
        else:
            file_index = i[0]

        # get UNC network path id of file
        id = self.file_id[file_index]

        # download tdms
        self._download(id)

    def _download(self, file_id: str) -> None:
        """Download the file id

        Parameter
        ---------
        file_id: str
            UNC (network path) of file
        """

        if self.download_filename is None:
            name = file_id + ".tdms"
        else:
            name = self.download_filename

        url = "/nifile/v1/service-groups/Default/files/{}/data".format(file_id)
        download = self.webService.get_route(url)
        open(name, "wb").write(download.content)


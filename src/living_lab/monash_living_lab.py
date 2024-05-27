import urllib3
from webservice import WebServices
from tdms_reader import TDMS

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

        # TODO add more features

        print("Connection established")

    def create_service(self, usn:str, pw:str):
        # Create the webService object
        webServices = WebServices(self.host_url)
        webServices.set_usr_pwd(usn, pw)

        return webServices

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


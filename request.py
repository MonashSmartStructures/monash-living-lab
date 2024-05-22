import os
import urllib3
import logging
import http.client as http_client

from webservice import WebServices
from open_tdms import TDMS
import requests
from configuration import configuration, username, password

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def create_service():
    # Connection Info
    host_url = "https://woodside-shm.eng.monash.edu"

    # Create the webService object
    webServices = WebServices(host_url)
    webServices.set_usr_pwd(username, password)

    return webServices


class MonashLivingLab:
    """Wrapper for Monash Living Lab's NI Systemlink API """

    def __init__(self):
        # init var
        self.data = None
        self.download_filename = None

        # create Living Lab webservice
        self.webService = create_service()
        self.host_url = "https://woodside-shm.eng.monash.edu"

        # get available tdms files
        available_file_url = "/nifile/v1/service-groups/Default/files?skip=0&take=0&orderBy=id&orderByDescending=false"
        query = self.webService.get_route(available_file_url)
        self.available_files = query.json()
        self.files = [file["properties"]["Name"] for file in self.available_files["availableFiles"]]
        self.file_id = [file["id"] for file in self.available_files["availableFiles"]]

        # get all tags

        # get all channels

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


if __name__ == '__main__':
    # file to download
    file_name = '202402181520_SHM-8.tdms'  # file to download

    # create main wrapper API object
    downloader = MonashLivingLab()

    # download
    downloader.get_tdms_file(filename=file_name)

    # read data
    td_data = TDMS(file_name)

    # Http API to use
    path = "SHM-1.WALK-3-Z"  # tag to query

    # download general
    url = "/nifile/v1/service-groups/Default/files/{}/data".format(2)  # To download files
    # tag = webServices.get_route(url)

    # tag general
    url = "/nitag"  # For tag
    get_tag = "/v2/tags/{}/values".format(path)
    # tag = webServices.get_route(url+get_tag)

    # tag api
    url = "/nifile"  # for files
    get_tag = "/v1/service-groups"
    # get tag
    # tag = webServices.get_route(url + get_tag)
    # print(tag.json())

    # download example
    # download = webServices.get_route("/nifile/v1/service-groups/Default/files/65c5763c4702427ecc90992a/data")
    # open("downtest.tdms","wb").write(download.content)

    print("done")

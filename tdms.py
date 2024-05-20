import numpy as np
from systemlink.clients.nifile.api.files_api import FilesApi
from systemlink.clients.nifile.models.query_available_files_request import QueryAvailableFilesRequest
from systemlink.clients.nifile.models.property_query import PropertyQuery

from systemlink.clients.nitdmreader.api.metadata_api import MetadataApi
from systemlink.clients.nitdmreader.api.data_api import DataApi
from systemlink.clients.nitdmreader.models.one_channel_specifier import OneChannelSpecifier
from systemlink.clients.nitdmreader.models.data_window import DataWindow
from systemlink.clients.nitdmreader.models.channel_specifications_xy_channels import ChannelSpecificationsXyChannels
from systemlink.clients.nitdmreader.models.channel_specifications import ChannelSpecifications
from systemlink.clients.nitdmreader.models.query_data_specifier import QueryDataSpecifier

from configuration import configuration

files_api = FilesApi(configuration)
metadata_api = MetadataApi(configuration)
data_api = DataApi(configuration)

file_name = "202405131140_SHM-1.tdms"
property_query = PropertyQuery(key="Name", operation="EQUAL", value=file_name)
query = QueryAvailableFilesRequest(properties_query=[property_query])
res = files_api.query_available_files(query=query)
# import matplotlib.pyplot as plt

import numpy as np
# import pandas as pd
import systemlink.clients.nitag as nitag
from systemlink.clients.nitaghistorian.api.history_api import HistoryApi
from systemlink.clients.nitaghistorian.models.http_query_request_body import HttpQueryRequestBody

from nisystemlink.clients.tag import DataType, TagManager
from nisystemlink.clients.core import HttpConfiguration
a = HttpConfiguration("https://woodside-shm.eng.monash.edu/",username="admin",password="WoodsideCivil")


tags_api = nitag.TagsApi(a)

tag_list = 'localhost.Health.CPU.MeanUsePercentage,localhost.Health.Memory.UsePercentage,localhost.Health.Disk.UsePercentage'
print(tags_api)
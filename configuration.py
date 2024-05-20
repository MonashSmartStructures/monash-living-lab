from nisystemlink.clients.core import HttpConfiguration
# from nisystemlink.clients.tag import DataType, TagManager
import json

with open('cred.json') as f:
    data = json.load(f)
    username = data['username']
    password = data['password']

configuration = HttpConfiguration("https://woodside-shm.eng.monash.edu/",username=username,password=password)

# mgr = TagManager(configuration)
# tag = mgr.open("SHM-1.WALK-3-Z", DataType.DOUBLE, create=False)
#
# read_result = mgr.read(tag.path)
# value = read_result.value
# print(value)
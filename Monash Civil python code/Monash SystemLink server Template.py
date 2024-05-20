from datetime import timedelta

from nisystemlink.clients.tag import DataType, TagManager
from nisystemlink.clients.core import HttpConfiguration

config = HttpConfiguration("https://woodside-shm.eng.monash.edu",None, "admin","WoodsideCivil",None)
mgr = TagManager(config)
tag = mgr.open("SHM-1.WALK-3-Z", DataType.DOUBLE, create=False)

read_result = mgr.read(tag.path)
value = read_result.value
print(value)
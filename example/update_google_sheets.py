"""Example to get read latest tag values and upload """

from living_lab import *
import json
from dateutil import parser

# load credentials
with open('../cred.json') as f:
    data = json.load(f)
    username = data['username']
    password = data['password']


# create main wrapper object
manager = MonashLivingLab(username, password)


# tag to request
request_body = {
  "path": "SHM-1.WALK-1-Beam1-LF",
  # "workspace": tag_properties['tag']['workspace'],
  # "startTime": "2024-05-30T05:00:18.0591889Z",
  # "endTime": "2024-05-30T05:10:46.742057Z",
  # "take": 1,
  # "continuationToken": "string",
  # "sortOrder": "ASCENDING"
}
jf = manager.get_tag_history(request_body=request_body)

# parse timestamp which are in ISO format
x = [parser.parse(f['timestamp']) for f in jf["values"]]
y = [float(f['value']) for f in jf["values"]]
print(jf)

# upload x and y data to google sheets


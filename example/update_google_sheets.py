"""Example to get read latest tag values and upload """
from datetime import datetime,timezone,timedelta
from google.oauth2.service_account import Credentials
import sys
sys.path.append("D:/syslink/pythonProject/src/")
sys.path.append("D:/syslink/pythonProject")
from living_lab import *
import json
from dateutil import parser
import gspread


scopes = [
    "https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"
]
cred = Credentials.from_service_account_file("../credential.json"
                                             ,scopes=scopes)
client = gspread.authorize(cred)

# load credentials
with open('../cred.json') as f:
    data = json.load(f)
    username = data['username']
    password = data['password']


# create main wrapper object
manager = MonashLivingLab(username, password)

# get local time and convert to UTC
now = datetime.now()
dt_now = datetime.now(timezone.utc) - timedelta(minutes=25)

# tag to request - tag name and start time
request_body = {
  "path": "SHM-6.DYN1-10X",
  # "workspace": tag_properties['tag']['workspace'],
  "startTime": dt_now.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),#"2024-05-31T03:57:00Z",
  # "endTime": "2024-05-30T05:10:46.742057Z",
  # "take": 1,
  # "continuationToken": "string",
  # "sortOrder": "ASCENDING"
}
tag_history = manager.get_tag_history(request_body=request_body)


# parse timestamp which are in ISO format
time_utc = [parser.parse(f['timestamp']) for f in tag_history["values"]]
z = [f['timestamp'] for f in tag_history["values"]]
y = [float(f['value']) for f in tag_history["values"]]
utctimestamp = [val.strftime("%H:%M:%S") for val in time_utc] # convert to AZ time zone
localtimestamp = [val.astimezone().strftime("%H:%M:%S") for val in time_utc]
print(tag_history)

# upload x and y data to google sheets
sheet_id = "1TyjUyso0LEYcfTSqNBGexOQRNApSmOxBUlmDVKYuf4U"
sheet = client.open_by_key(sheet_id)
#sheet.sheet1.delete_rows(1,2)
sheet.sheet1.update([localtimestamp,y],"1:2")
values = sheet.sheet1.row_values(1)
print(values)

from living_lab.monash_living_lab import MonashLivingLab,TDMS
import json

# load credentials
with open('cred.json') as f:
    data = json.load(f)
    username = data['username']
    password = data['password']

# name of tdms to download
file_name = '202402181520_SHM-8.tdms'

# create main wrapper object
manager = MonashLivingLab(username, password)

# download
manager.get_tdms_file(filename=file_name)

# read data
td_data = TDMS(file_name)

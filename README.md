# Monash Living Lab Wrapper
This module is an API wrapper for NI-Systemlink web interface.


First, create a `cred.json` file storing the username and password credentials, 
which is then read automatically by the `configureation.py` module.
An example of a `cred.json` file is as shown:

```cloudfoundry
{"username": "user","password":"pw123"}
```

In a Python script, import the entire `monash_living_lab` module :

```
from monash_living_lab import *
```

To download a TDMS file from NI systemlink, simply create the ``MonashLivingLab`` object and
and run as follows:

```
file_name = '202402181520_SHM-8.tdms'  

manager = MonashLivingLab() 

manager.get_tdms_file(file_name)

```

This downloads the `202402181520_SHM-8.tdms` file onto the current working directory.
This TDMS file can then be read using the `TDMS` object as follow:

```
tdms = TDMS(file_name)
```

The following attributes can be accessed from the `TDMS` object:

```
tdms.channel_names # names of all the channel
tdms.data # dictionary of raw data of the various channel names
tdms.timestamp # timestamp of raw data
tdms.properties # dictionary of properties such as sampling intervals

```

To get a tag history from NI-Systemlink:

```
tag_history = manager.get_tag_history(request_body=request_body)

```

where `request_body` is a dictionary containing the request details of the tag - at a minimum provide the Tag's ``path`` and ``startTime``:

```
request_body = {
  "path": "SHM-6.DYN1-10X",
  "startTime": "2024-05-31T03:57:00Z",
  "endTime": "2024-05-31T05:57:00Z", 
```

**_NOTE:_**  As of version 0.1.0, the `startTime` and `endTime` argument needs to be in UTC time zone 

To read a Tag value at the current time:

```
value = manager.get_tag_values(tagname="SHM-6.DYN1-10X")
```





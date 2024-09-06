from nptdms import TdmsFile
import numpy as np
import pandas as pd

class TDMS:
    """Class to read tdms files """

    def __init__(self, filename: str):
        self.filename = filename

        # read tdms
        self._extract_tdms()

    def _extract_tdms(self):
        """Extract data from tdms file"""

        channels = {}
        properties = {}
        channel_names =[]

        tdms_file = TdmsFile.read(self.filename)
        for group in tdms_file.groups():
            group_name = group.name
            for channel in group.channels():
                channel_name = channel.name
                # Access dictionary of properties:
                properties[channel_name] = channel.properties
                # Access numpy array of data for channel:
                data = channel[:]
                channels[channel_name] = data
                channel_names.append(channel_name)
        # ref start time and increment (all channels same timestamp)
        start_time = channel.properties["wf_start_time"]
        increment = channel.properties["wf_increment"]
        num_increments = len(data)

        # Typical sampling interval = 0.0018 seconds
        timedelta = np.timedelta64(int(increment * 1e6), 'us') # convert to timedelta64 object

        # create time stamp array
        self.time_stamp = [start_time + i * timedelta for i in range(num_increments)]
        self.channel_names = channel_names
        self.data = channels
        self.properties = properties
        print("Read successful file - {}".format(self.filename))

    def get_csv(self)->None:
        """Writes the data into a csv file with same filename defined for tdms"""
        # ensure all columns have same array
        max_array_len = max([len(array) for array in self.data.values()])
        # ensure all arrays are same length
        for channelname,array in self.data.items():
            if len(array)<max_array_len:
                # add zero padding to array up to max array length
                self.data[channelname] = np.pad(array,(0,max_array_len-len(array)))
        df = pd.DataFrame.from_dict(self.data)
        df.to_csv("file.csv")
        print("Write " + self.filename + " to csv - completed")


if __name__ == '__main__':
    # have the tdms or path to tdms
    tdms_data = TDMS("../../202402181520_SHM-8.tdms")

    # do stuff with data
    tdms_data.data


from nptdms import TdmsFile
import numpy as np

class TDMS:
    """Class to read tdms files """
    def __init__(self, filename: str):
        self.filename = filename

        # reads
        self._read()

    def _read(self):
        """Extract data from tdms file"""

        channels = {}
        properties = {}

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

        # ref start time and increment (all channels same timestamp)
        start_time = channel.properties["wf_start_time"]
        increment = channel.properties["wf_increment"]
        num_increments = len(data)

        # Typical sampling interval is 0.0018 seconds
        timedelta = np.timedelta64(int(increment*1e6),'us')

        # create time stamp array
        self.time_stamp = [start_time + i * timedelta for i in range(num_increments)]

        # store
        self.data = channels
        self.properties = properties
        print("done")

    def create_time_stamp(self):
        ...


if __name__ == '__main__':
    # have the tdms or path to tdms
    data = TDMS("202402181520_SHM-8.tdms")

    # do stuff with data

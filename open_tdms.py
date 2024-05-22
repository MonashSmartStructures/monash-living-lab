from nptdms import TdmsFile


class TDMS:
    """Class to read tdms files """
    def __init__(self, filename: str):
        self.filename = filename

        # reads
        self._read()

    def _read(self):
        tdms_file = TdmsFile.read(self.filename)
        for group in tdms_file.groups():
            group_name = group.name
            for channel in group.channels():
                channel_name = channel.name
                # Access dictionary of properties:
                properties = channel.properties
                # Access numpy array of data for channel:
                data = channel[:]

        self.data = data
        self.properties = properties
        self.channel_name = channel_name
        print("done")
        print(data)

    def create_time_stamp(self):
        ...


if __name__ == '__main__':
    # have the tdms or path to tdms
    data = TDMS("202402181520_SHM-8.tdms")

    # do stuff with data

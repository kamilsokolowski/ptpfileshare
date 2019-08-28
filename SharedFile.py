import os
import hashlib


class SharedFile:
    """
        This class represents file that is going to be shared in network
        Attributes:
            str:path         : path to shared file.
            file_holder      : handle to file.
            int:size         : size of the file.
            int:segment_size : size in bytes of single segment to send over network.
            str:segments_hashes : list of segment hashes of shared file.
            byte:segments    : list of file segments.
        Constructor:
            str:path : path to shared file
            int:segment_size : size of segment in bytes
        Methods:
            create_hash_table_of_file : builds list of segments_hashes
    """
    def __init__(self, path, segment_size):
        # Constructor which holds handle to file and basic information about file.
        self.path = path
        self.file_holder = open(path, 'rb')
        self.size = os.stat(path).st_size
        self.segment_size = segment_size
        self.segments_hashes = []  # array for hashes of segments of shared file
        self.segments = []  # file fragmented into segments to send over network in array
        self.create_hash_table_of_file()

    def create_hash_table_of_file(self):
        # Method which is responsible for building segments_hashes list.
        # It uses md5 hash function to generate sums for segement validation.
        with self.file_holder as f:
            segment_hash = hashlib.md5()
            segment = f.read(self.segment_size)  # get segment
            segment_hash.update(segment)
            self.segments_hashes.append(segment_hash.hexdigest())  # calculate hash and add to array
            self.segments.append(segment)
            while segment:  # continue until file's end
                segment_hash = hashlib.md5()
                segment = f.read(self.segment_size)
                segment_hash.update(segment)
                self.segments_hashes.append(segment_hash.hexdigest())
                self.segments.append(segment)

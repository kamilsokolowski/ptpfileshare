import os
import hashlib
class SharedFile:
    #path - path to shared file
    #segment_size - size in bytes of single segment to send over network
    def __init__(self, path, segment_size):
        self.path = path
        self.file_holder = open(path, 'rb')
        self.size = os.stat(path).st_size
        self.segment_size = segment_size
        self.create_hash_table_of_file()

    def create_hash_table_of_file(self):
        self.segments_hashes = [] #array for hashes of segments of shared file
        self.segments = [] #file fragmented into segments to send over network in array
        with self.file_holder as f:
            segment_hash = hashlib.md5()
            segment = f.read(self.segment_size)#get segment
            segment_hash.update(segment)
            self.segments_hashes.append(segment_hash.hexdigest())#calculate hash and add to array
            self.segments.append(segment)
            while segment:#continue until file's end
                segment_hash = hashlib.md5()
                segment = f.read(self.segment_size)
                segment_hash.update(segment)
                self.segments_hashes.append(segment_hash.hexdigest())
                self.segments.append(segment)
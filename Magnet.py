import json

"""
    This class represents data about file which are necessary for peer to connect
    Attributes:
        str:name         : name of shared file
        int:size         : size of the file.
        int:segment_size : size in bytes of single segment to send over network.
        str:segments_hashes : list of segment hashes of shared file.
        int:segment_count: number of segments
        dict:tracker_list : dictionary containing information about trackers network in following format
                                { ip: [STATUS, public_key]} where ip is the ip of tracer and the value is
                                list 2 elements status of tracker(True or False) and it's Public key to
                                verify digital signature.
    Constructor:
        str:path : path to magnet file
        or
        str:name         : name of shared file
        int:size         : size of the file.
        int:segment_size : size in bytes of single segment to send over network.
        str:segments_hashes : list of segment hashes of shared file.
        int:segment_count: number of segments
        dict:tracker_list : dictionary containing information about trackers network in following format
                                { ip: [STATUS, public_key]} where ip is the ip of tracer and the value is
                                list 2 elements status of tracker(True or False) and it's Public key to
                                verify digital signature.
    Methods:
        generate_magnet_file : save all data from object in magnet file
"""
class Magnet:
    def __init__(self, *args):
        if len(args) == 1:
            with open(args[0], 'r') as magnet_file:
                magnet_list = json.load(magnet_file)
            self.name = magnet_list[0]
            self.size = magnet_list[1]
            self.segment_size = magnet_list[2]
            self.segment_count = magnet_list[3]
            self.segments_hashes = magnet_list[4]
            self.tracker_list = magnet_list[5]
        else:
            self.name = args[0]
            self.size = args[1]
            self.segment_size = args[2]
            self.segment_count = args[3]
            self.segments_hashes = args[4]
            self.tracker_list = args[5]


    def generate_magnet_file(self):
        magnet_list = [self.name, self.size, self.segment_size, self.segment_count, self.segments_hashes, self.tracker_list]
        print(magnet_list)
        magnet_file_name = str(self.name + '_magnet.json')
        with open(magnet_file_name, 'w') as magnet_file:
            json.dump(magnet_list, magnet_file)


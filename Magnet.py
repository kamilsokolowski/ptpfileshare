class Magnet:
    def __init__(self, name, size, segment_size, segment_count, segments_hashes, tracker_list):
        self.name = name
        self.size = size
        self.segment_size = segment_size
        self.segment_count = segment_count
        self.segments_hashes = segments_hashes
        self.tracker_list = tracker_list


class SharedFile:
    def __init__(self, path):
        self.path = path
        self.file_holder = open(path, 'r')

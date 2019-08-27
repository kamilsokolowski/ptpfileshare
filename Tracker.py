#class for trusted node called tracker
#keep updating lists of seeds and peers
#has 100% complete file
#has RSA digital signature
class Tracker:
    def __init__(self, ip ):
        self.ip = ip

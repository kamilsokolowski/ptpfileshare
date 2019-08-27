from Crypto.PublicKey import RSA
import socket
import os
#class for trusted node called tracker
#keep updating lists of seeds and peers
#has 100% complete file
#has RSA digital signature
class Tracker:
    def __init__(self):
        gw = os.popen("ip -4 route show default").read().split()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((gw[2], 0))
        self.ip = s.getsockname()[0]
        self.key = RSA.generate(2048)
        self.tracker_list = {}
        self.tracker_list.update({self.ip: True})
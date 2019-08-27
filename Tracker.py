from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from SharedFile import SharedFile
import json
import socket
import os
#class for trusted node called tracker
#keep updating lists of seeds and peers
#has 100% complete file
#has RSA digital signature
class Tracker:
    def __init__(self, path):
        segment_size = 4 #size in bytes of single file segment
        gw = os.popen("ip -4 route show default").read().split() #magic for obtain local ip add
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #magic for obtain local ip add
        s.connect((gw[2], 0)) #magic for obtain local ip add
        self.ip = s.getsockname()[0] #magic for obtain local ip add
        self.key = rsa.generate_private_key(65537,2048,default_backend())
        self.tracker_list = {} #list of active trackers
        self.tracker_list.update({self.ip:
        [True, self.key.public_key().public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.PKCS1).decode('utf-8')
        ]}) #adding itself as active tracker
        self.shared_file = SharedFile(path, segment_size) #create file to share
        self.create_config_file_for_new_trackers()


    def create_config_file_for_new_trackers(self):
        with open('tracker_config.json', 'w') as f:
            json.dump(self.tracker_list,f)
        #key = load_pem_public_key(self.tracker_list.get('192.168.0.208')[1].encode(),default_backend()) future me will thank me for this line

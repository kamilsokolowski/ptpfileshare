import json
import socket
import os
from Magnet import Magnet

# from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from SharedFile import SharedFile

# class for trusted node called tracker
# keep updating lists of seeds and peers
# has 100% complete file
# has RSA digital signature


class Tracker:
    """
        Peer to peer tracker class. Purpose of this class is to be root of protocol.
        It contains information about tracer network, cryptographic keys and file details.
        Attributes:
            str:ip            : ip address of tracer.
            RSAPrivateKey:key : RSA 2048 bit key pair (Pk, Sk).
            dict:tracker_list : dictionary containing information about trackers network in following format
                                { ip: [STATUS, public_key]} where ip is the ip of tracer and the value is
                                list 2 elements status of tracker(True or False) and it's Public key to
                                verify digital signature.
            SharedFile:shared_file : Class which represents file that is going to be shared in the network.
            Magnet:magnet_file : Class which represents all data about file required by peer to connect
        Constructor:
            str:path         : path to shared file.
            int:segment_size : size of segments to which is file going to be divided. (default size is 1024 bytes)
        Methods:
            create_config_file_for_new_trackers : This method serializes tracker list into json format file.
    """
    def __init__(self, path, segment_size=1024, config_json_path=''):
        # Constructor for Tracer class. Constructor obtains ip address of net card and fill ip field.s
        gw = os.popen("ip -4 route show default").read().split()  # magic for obtain local ip add
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # magic for obtain local ip add
        s.connect((gw[2], 0))  # magic for obtain local ip add
        self.ip = s.getsockname()[0]  # magic for obtain local ip add
        self.key = rsa.generate_private_key(65537, 2048, default_backend())
        if config_json_path == '':
            self.tracker_list = {}  # list of active trackers
        else:
            with open(config_json_path, 'r') as config_json:
                self.tracker_list = json.load(config_json)
        self.tracker_list.update(
            {
                self.ip: [
                    True,
                    self.key.public_key().public_bytes(
                        serialization.Encoding.PEM,
                        serialization.PublicFormat.PKCS1).decode('utf-8')
                    ]
            }
        )  # adding itself as active tracker
        self.shared_file = SharedFile(path, segment_size)  # create file to share
        self.create_config_file_for_new_trackers() # create new config file for new trackers
        self.magnet_file = Magnet(
            self.shared_file.file_name,
            self.shared_file.size,
            self.shared_file.segment_size,
            self.shared_file.segment_count,
            self.shared_file.segments_hashes,
            self.tracker_list) # create magnet data structure
        self.magnet_file.generate_magnet_file() #create magnet file for peers to connect

    def create_config_file_for_new_trackers(self):
        # Method for serializing tracer list into json file.
        with open('tracker_config.json', 'w') as f:
            json.dump(self.tracker_list, f)
            # self.tracker_list = json.load(f)
        """key = load_pem_public_key(
            self.tracker_list.get('192.168.0.208')[1].encode(),
            default_backend()
        ) future me will thank me for this line"""

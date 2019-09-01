from Magnet import Magnet
import subprocess
"""
    This class represents nodes of p2p network
    Attributes:
        Magnet:magnet   :  Class which represents all data about file required by peer to connect
        
    Constructor:
        Magnet:magnet   : It is adding magnet file to peer structure
    Methods:
        get_avg_ping    : From ip_list returns best 3 pings to classify best nodes of network
"""
class Peer:
    def __init__(self, path_to_magnet):
        self.magnet = Magnet(path_to_magnet)


    def get_avg_ping(self, ip_list):
        # Metod which is used to create list of best pings with thier ip
        sorted_list_with_ping = []

        for ip in ip_list:
            s = subprocess.run(["ping", "-c 4", ip[0]], stdout=subprocess.PIPE)
            data_from_ping = str(s.stdout)
            sorted_list_with_ping.append((data_from_ping.split("/")[4],ip))
        sorted_list_with_ping.sort()
        if len(ip_list) < 3:
            return sorted_list_with_ping
        else:
            return sorted_list_with_ping[0:4]







from Magnet import Magnet
import subprocess

class Peer:
    def __init__(self, path_to_magnet):
        self.magnet = Magnet(path_to_magnet)


    def get_avg_ping(self, ip):
        # Metod which is used to create list of best pings with thier ip
        sorted_list_with_ping = []
        for i in ip:
            s = subprocess.run(["ping", "-c 4", i[0]], stdout=subprocess.PIPE)
            data_from_ping = str(s.stdout)
            sorted_list_with_ping.append((data_from_ping.split("/")[4],i))
        sorted_list_with_ping.sort()
        top_3_ping_with_ip = sorted_list_with_ping[0:4]
        return top_3_ping_with_ip






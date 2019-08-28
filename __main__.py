# from SharedFile import SharedFile
from Tracker import Tracker


# print("1. Create first tracker and config file")
# print("2. Create tracker from config file")
# choice = input("->")
# path = input("Enter path to file to share")
# if choice == '1':
#    my_tracker = Tracker(path)
#my_tracker = Tracker('/home/misterk/Desktop/lorem.txt')
my_tracker = Tracker('/home/misterk/Desktop/lorem.txt', 1024, 'tracker_config.json')


#!/usr/bin/python3

import datetime
import os

class Journal():
    """
    Class to implement the whole Journaling Schedule.
    """
    def __init__(self, details, fileName = 'log.txt'):
	info = ['NetworkAddress', 'Netmask', 'TaskName', 'ParameterServers', 'WorkerServer']        
	info   = ' |'.join(["{}-{}".format(x,y) for x,y in zip(info,details)])
        header = ','.join(['timestamp', 'Type', 'Id', 'memoryShare', 'Port'])
        self.time   = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H_%M_%S')
        self.index = len(os.listdir('/mnt/logs/txtlogs'))
        with open(root_path+'/mnt/logs/txtlogs/log' + self.time +'.txt', 'a') as file:
            file.write(info +  '\n')
            file.write(header + '\n')
              
    def writeToFile(self, listOfParams):
        assert len(listOfParams) == 5 "Parameter list has too many/missing elements"
        with open(root_path+'/mnt/logs/txtlogs' + self.time + '.txt', 'a') as file:
            file.write(','.join([str(x) for x in listOfParams]) + ','+str(self.index) +'\n')

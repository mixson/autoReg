import os
import sys
from datetime import datetime
from values import CONSTANT

# def getProjectFullPath():
#     APPLICATION_NAME = "Sensor_Application"
#     FULLPATH_ENDINDEX = os.getcwd().index(APPLICATION_NAME) + APPLICATION_NAME.__len__()
#     APPLICATION_NAME_FULL_PATH = os.getcwd()[0:FULLPATH_ENDINDEX]
#     return APPLICATION_NAME_FULL_PATH
#
# APPLICATION_NAME_FULL_PATH = getProjectFullPath()
# sys.path.append(APPLICATION_NAME_FULL_PATH)

APPLICATION_NAME_FULL_PATH = CONSTANT.APPLICATION_NAME_FULL_PATH
sys.path.append(APPLICATION_NAME_FULL_PATH)

class Logger():
    # targetLocation = os.path.join(APPLICATION_NAME_FULL_PATH, "log", "Monitor{}.log".format(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")))
    targetLocation = os.path.join(APPLICATION_NAME_FULL_PATH, "log", "Monitor.log")
    def __init__(self):
        print("Logger wrote at {}".format(Logger.targetLocation))
        self.cursor = None

    def setTargetLocation(self, targetLocation):
        self.targetLocation = targetLocation
        return self

    @staticmethod
    def write(data):
        with open(Logger.targetLocation, "a+") as file:
            file.write(str(data))

    @staticmethod
    def dwrite(data):
        with open(Logger.targetLocation, "a+") as file:
            file.write("[{}]: {} \n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(data)))

    @staticmethod
    def dwriteprint(data):
        print(data)
        with open(Logger.targetLocation, "a+", encoding="utf-8") as file:
            file.write("[{}]: {} \n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(data)))
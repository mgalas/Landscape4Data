import abc, requests, json


class CleanOrganise(metaclass=abc.ABCMeta):
    dataFromFile = []
    organisedData = []
    header = []
    groupCounter = 0 #for testing

    def __init__(self,d):
        self.dataFromFile = []
        self.organisedData = []
        self.header = []
        self.dataFromFile = d
        self.header = self.dataFromFile[0]
        self.dataFromFile = self.dataFromFile[1:]
        self.organisedData = []
        self.groupCounter = 0



    @abc.abstractmethod
    def apiCall(self,item):
        pass



    @abc.abstractmethod
    def cleanData(self,dataValue):
        pass

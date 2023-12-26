
class mvcModel:
    def __init__(self):
        self.ipAddress = None  # Initial value for the attribute
        self.subnetMask = None  # Initial value for the attribute
        self.hostname = None  # Initial value for the attribute

    def getIp(self):
        return self.ipAddress

    def getMask(self):
        return self.subnetMask

    def setIp(self, ipAddress):
        self.ipAddress = ipAddress

    def setMask(self, subnetMask):
        self.subnetMask = subnetMask

    def getHostname(self):
        return self.hostname

    def setHostname(self, hostname):
        self.hostname = hostname
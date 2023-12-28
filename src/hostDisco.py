import math
import socket
import struct
from ping import Ping
import sys
class host_discovery:
    def __init__(self, model, subnetMask = 24, ipAddress = '127.0.0.1'):
        self.model = model
        self.subnetMask = subnetMask
        self.ipAddress = ipAddress
        self.discovered_hosts = []
    
    def ipAddress_rangeCalc(self):
        if self.subnetMask == 0:
            raise ValueError("Subnet is empty")

        totalBits = 32 - self.subnetMask
        total_hosts = int(math.pow(2, totalBits)) - 2
        return total_hosts
    def genHosts(self):
        # Calculate the total number of hosts based on the subnetMask
        total_hosts = self.ipAddress_rangeCalc()
        hostAddresses = []
        
        # Convert the IP address to a byte array
        ipAddressBytes = struct.unpack('!L', socket.inet_aton(self.ipAddress))[0]
        
        # Ierate over the range of total hosts
        for i in range(1, total_hosts + 1):
            # Calculate the host IP address by changing the last byte in the ip in thebyte array
            hostIp = ipAddressBytes & 0xFFFFFF00 | i
            # Convert back to a a string
            hostAddress = socket.inet_ntoa(struct.pack('!L', hostIp))
            # Add the host address to the list
            hostAddresses.append(hostAddress)

        return hostAddresses
    def pingSweep(self):
        hostAddresses = self.genHosts()
        total_hosts = len(hostAddresses)
        print(f"Scanning {total_hosts} hosts")
        for index, ipAddress in enumerate(hostAddresses):
            percent_complete = int(((index + 1) / total_hosts) * 100)  
            sys.stdout.write(f'\r{percent_complete}% complete')
            sys.stdout.flush()
            pinger = Ping(ipAddress)
            pinger.ping()
            if pinger.ping_results:
                self.discovered_hosts.append(ipAddress)
        return self.discovered_hosts
   

if __name__ == "__main__":
    model = None
    subnetMask = 24
    ipAddress = '192.168.1.0'
    discovery = host_discovery(model, subnetMask, ipAddress)
    total_hosts = discovery.ipAddress_rangeCalc()
    hostAddresses = discovery.genHosts()
    discovery.pingSweep()
    for hosts in discovery.discovered_hosts:
        print("\n" +hosts + " is up")

import socket
from loadServices import LoadServices
import sys

class portScanner:
    def __init__(self, ipAddress='127.0.0.1', startPort=1, endPort=65535):
        self.services = LoadServices()
        self.ipAddress = ipAddress
        self.startPort = startPort
        self.endPort = endPort
        self.activeServices = {}
        self.scan()

    def scan(self):
        print("scanning ports")
        for port in range(self.startPort, self.endPort + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((self.ipAddress, port))
            if result == 0:
                try:
                    service_name = self.services.getServiceMap().get(str(port), "Unknown service")
                    self.activeServices[port] = service_name
                except Exception as e:
                    print(f"Error retrieving service for port {port}: {e}")
                finally:
                    sock.close()
                
        for port, service in self.activeServices.items():
            print(f"Port {port} is open: {service}")
        sys.stdout.flush()

if __name__ == "__main__":
    ipAddress = '192.168.1.254'  
    startPort = 1
    endPort = 1024  
    scanner = portScanner(ipAddress, startPort, endPort)
import subprocess
import platform

class Ping:  
    def __init__(self, ipAddress):
        self.ipAddress = ipAddress  
        self.ping_results = None
    def ping(self, timeout=0.02):
        
        if platform.system() == 'Windows':
            ping_command = ['ping', '-n', '1', self.ipAddress, '-w', str(timeout * 1000)]
        else:
            ping_command = ['ping', '-c', '1', self.ipAddress, '-W', str(timeout)]
        
        try:
            ping_results = subprocess.run(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
            self.ping_results = ping_results.returncode == 0
        except subprocess.TimeoutExpired:
            self.ping_results = False
        return self.ping_results
  
if __name__ == "__main__":
    ipAddress = '192.168.1.254'
    ping = Ping(ipAddress)  
    ping.ping()  


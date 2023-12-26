import os
class LoadServices:
    def __init__(self):
        self.serviceMap = {}
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.ports_list = os.path.join(current_dir, 'resources', 'ports.txt')
    def load(self):
        with open(self.ports_list, "r") as services:
            for line in services:
                parts = line.strip().split()
                if len(parts) >= 3:
                    key = parts[0]
                    value = parts[2]
                    self.serviceMap[key] = value

    def getServiceMap(self):
        if not self.serviceMap:  
            self.load()
        return self.serviceMap

if __name__ == "__main__":
    loader = LoadServices()
    service_map = loader.getServiceMap()

    for key, value in service_map.items():
        print(f"Key: {key}, Value: {value}")

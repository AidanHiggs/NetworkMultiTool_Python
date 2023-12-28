from scapy.all import ARP, Ether, srp
import hostDisco as host_discovery

class AddMac:
    def __init__(self, model, ipAddress='192.168.1.254', subnetMask=24):
        self.mac = None
        self.ips = []
        self.macs = []
        self.model = model
        self.ipAddress = ipAddress
        self.host_discovery = host_discovery.host_discovery(model, subnetMask, ipAddress)
        self.subnetMask = subnetMask
        self.hostAddress = []

    def add_mac(self, ipAddress):
        arp_request = ARP(pdst=ipAddress)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        if answered_list:
            ip = answered_list[0][1].psrc
            mac = answered_list[0][1].hwsrc
            #print("host: " + ip + " is up\n" "    MAC address: "  + mac)  
        else:
            ip = ipAddress
            mac = None
        self.ips.append(ip)
        self.macs.append(mac)
        return self.macs


    def macDec(self):
        discovered_hosts = self.host_discovery.pingSweep()
        for host_address in discovered_hosts:
            self.add_mac(host_address)
        for ip, mac in zip(self.ips, self.macs):
            print(f"host: {ip} is up\n    MAC address: {mac}")
            if mac is None:
                print(f"host: {ip} is up\n    MAC resolution failed")
                

if __name__ == "__main__":
    model = None
    ipAddress = '192.168.1.254'
    subnetMask = 24
    add_mac_instance = AddMac(model, ipAddress, subnetMask)
    add_mac_instance.macDec()  # This will perform the ping sweep and add MACs.
import sys
import model
class mvcViewFacade:
    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
    def start(self):
        if len(sys.argv) > 1:
            for arg in sys.argv[1:]:
                self.controller.scanMethods(selection)
        else:
            while True:
                self.menu()
                selection = input("Select scan method: ")
                print("Selected: " + selection)
                self.controller.scanMethods(selection)
                if selection.lower() == 'exit':
                    break
            self.menu2()

    def menu(self):
        print("Select scan method:")
        print("1. Host discovery")
        print("2. Port scan")
        print("3. Tracert whois")
        print("4. Ping")
        print(" type 'exit' to Exit")


def menu2(self):
    ip_input = input("Enter IP address or hostname: ")
    ip_regex = re.compile(
        r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    )
    if not re.match(ip_regex, ip_input):
        self.ipAddress = socket.gethostbyname(ip_input)
        mvcModel.setIp(self, self.ipAddress)
    else:
        mvcModel.setIp(self, ip_input)
    
    mask_input = input("Enter subnet mask: ")
    mvcModel.setMask(self, mask_input)


""" if __name__ == "__main__":
    controller = mvcController() # Assuming you have an appropriate constructor for this
    model = mvcModel() # Replace with actual model
    portScanner = None # Replace with actual portScanner
    ping = None # Replace with actual ping
    hostDiscovery = None # Replace with actual hostDiscovery

    view = mvcViewFacade(controller, model, portScanner, ping, hostDiscovery)
    view.start()
     """
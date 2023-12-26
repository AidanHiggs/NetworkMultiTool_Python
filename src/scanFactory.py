class scanFactory:
    def __init__(self, model, port_scanner, ping_decorator, host_discovery):
        self.model = model
        self.port_scanner = port_scanner
        self.ping_decorator = ping_decorator
        self.host_discovery = host_discovery
    def scanFactory(scanMethod): 
        #  factory for selected scan methods from controller.mvcController.py  
        if scanMethod == '1':
            print ("Performing host discovery")
            
        if scanMethod == '2':
                    pass
        if scanMethod == '3':
                    pass
        if scanMethod == '4':
                    pass
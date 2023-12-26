from model import mvcModel
from view import mvcViewFacade
class mvcController:
    def __init__(self, model):
        self.model = model
        self.view = mvcViewFacade(self, self.model)
    def perfScan(self, scanMethods):
        match scanMethods:
            case scanMethods.HOST_DISCOVERY:
                self.performPortScan()
            case scanMethods.PORT_SCAN:
                self.performPing()
            case scanMethods.TRACERT_WHOIS:
                self.performTracert()
            case scanMethods.PING:
                self.performPing()
            case _:
                print("Invalid scan method")
                perfScan()
    def performPortScan():
        scanFactory("port scan")
    def passperformPing():
        scanFactory("ping")
    def performTracert():
        scanFactory("tracert")
    def performHostDiscovery():
        scanFactory("host discovery")
    def scanMethods(selection, scanFactory):
        print(selection)
        HOST_DISCOVERY = 1
        PORT_SCAN = 2
        TRACERT_WHOIS = 3
        PING = 4

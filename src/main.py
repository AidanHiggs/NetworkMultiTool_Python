import sys
sys.path.append('/home/aidan/Documents/projects/networkscanner/src')
from model import mvcModel
from controller import mvcController
from view import mvcViewFacade
import portScanner as portScanner
import hostDisco as hostDiscovery
from loadServices import LoadServices

class Main:
    def __init__(self):
        model = mvcModel()
        controllerInstance = mvcController(model)
        view = mvcViewFacade(controllerInstance, model)
        view.start()

if __name__ == "__main__":
    Main()

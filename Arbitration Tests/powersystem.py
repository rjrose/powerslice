import powerpool, powerport
class PowerSystem():
    #define powersystem with a power pool and a number of ports
    def __init__(self, numPorts, totalStorage):
        self.pool = powerpool.PowerPool(totalStorage)
        self.port = []
        for i in range(numPorts):
            self.port.append(powerport.PowerPort)
        # self.port[numPorts] = powerport.PowerPort
    def printState(self):
        print("Pool: ")
        self.pool.printState()
        for i in range(len(self.port)):
            print("Port " + str(i) + ":")
            self.port[i].printState()
    # def plug(self, id, requestedPower):
    #     if self.port[id].connected == True:
    #         return False
    #     elif self.pool.request(requestedPower):
    #         self.port[id].connected = True
    #         self.port[id].activePower = requestedPower
    #         return True
    #     else:
    #         return False



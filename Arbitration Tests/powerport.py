class PowerPort:
    #initialize power port
    #port consists of current power allocated to port, and reserved power
    def __init__(self):
        #self.id = id
        self.connected = False
        self.activePower = 0
        self.reservedPower = 0
    def printState(self):
        print("Connected: " + str(self.connected) + " Active power: " + str(self.activePower) + " Reserved power: " + str(self.reservedPower))
        
    
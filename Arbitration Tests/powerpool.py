class PowerPool:
    #initialize available power to specified size of pool
    def __init__(self,size):
        self.maxPower = size
        self.availablePower = size
        print("Pool Created! Available power: "+ str(self.availablePower))
    #request to use a portion of the pool, if request is les than or equal to available power
    #then it is granted
    def request(self,amount):
        if amount<=self.availablePower:
            self.availablePower = self.availablePower - amount
            print("Request approved! Available power: " + str(self.availablePower))
            return True
        else:
            print("Request denied! Available power: " + str(self.availablePower))
            return False
    #release previously allocated power back to the pool
    def release(self,amount):
        if (self.availablePower + amount) > self.maxPower:
            print("Error! Original size of pool exceeded")
            return False
        else:
            self.availablePower = self.availablePower + amount
            print("Power Released! Available power: " + str(self.availablePower))
            return True
    def printState(self):
        print(str(self.availablePower) + " is available out of " + str(self.maxPower))
        
    
   
   
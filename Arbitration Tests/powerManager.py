def connect(port, label, maxDraw):
    portList[port] = (label,maxDraw,0)
    if maxDraw <= poolAvail:
        poolAvail -= maxDraw
        portList[port][2] = maxDraw
    else:
        temp = poolAvail
        poolAvail = 0
        portList[port][2] = temp
        
def printPool():


poolMax = 100
poolAvail = poolMax
numPorts = 5
portList = []
for i in range(numPorts)
    #Port: label, MaxDraw, ActualDraw
    newPort = ("label",0,0)
    portList.append(newPort)


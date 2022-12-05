deviceDict = {}
poolMax = 100
poolAvail = poolMax
def connect(label, maxDraw):
    global poolAvail
    if maxDraw <= poolAvail:
        poolAvail -= maxDraw
        currentDraw = maxDraw
    else:
        temp = poolAvail
        poolAvail = 0
        currentDraw = temp
    deviceDict[label] = {'maxDraw':maxDraw,'currentDraw':currentDraw}

def disconnect(label):
    global poolAvail
    tempDraw = deviceDict[label]['currentDraw']
    deviceDict.pop(label)
    poolAvail += tempDraw

def balance():
    global poolAvail, poolMax
    maxDrawTotal = 0
    for label in deviceDict.keys():
        maxDrawTotal += deviceDict[label]['maxDraw']
    #under power fraction: poolMax/maxDrawTotal
    underPF = poolMax/maxDrawTotal
    if underPF>=1:
        poolAvail = poolMax-maxDrawTotal
        for label in deviceDict.keys():
            deviceDict[label]['currentDraw'] = deviceDict[label]['maxDraw']
    else:
        poolAvail = 0
        for label in deviceDict.keys():
            deviceDict[label]['currentDraw'] = underPF*deviceDict[label]['maxDraw']



while True:
    inString = input('Connect, disconnect, balance, print, or quit?\n')
    if inString == 'connect':
        inLabel = input('Label: ')
        inDraw = int(input('Max power draw: '))
        connect(inLabel,inDraw)
    elif inString == 'disconnect':
        inLabel = input('Label: ')
        disconnect(inLabel)
    elif inString == 'balance':
        balance()
    elif inString == 'print':
        print("Available power: " + str(poolAvail))
        print(deviceDict)
    elif inString == 'quit':
        break
    else:
        print('Invalid statement. Try again.')





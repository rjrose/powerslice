#Setup: Import pyplot, initialize device dictionary and power pool
import matplotlib.pyplot
deviceDict = {}
poolMax = 100
poolAvail = poolMax
#Adds device to dictionary, assigns max draw if able and if not assigns remaining power
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
#Removes device from dictionary, returns current draw to available power pool
def disconnect(label):
    global poolAvail
    tempDraw = deviceDict[label]['currentDraw']
    deviceDict.pop(label)
    poolAvail += tempDraw
#Takes the sum of all max draws for all devices. If able, allocates max power to all devices. 
# If not, assigns each device the same percentage of their max power, leaving no unallocated power available.
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
#Plots all devices in a pie chart to show allocation of the total power pool.
def plotPower():
    global poolAvail
    powLabels = ['Unallocated']
    powData = [poolAvail]
    for label in deviceDict.keys():
        powLabels.append(label)
        powData.append(deviceDict[label]['currentDraw'])
    matplotlib.pyplot.pie(powData, explode=None, labels=powLabels, colors=None, autopct='%1.1f%%', shadow=False)
    #matplotlib.pyplot.legend()
    matplotlib.pyplot.show()



#Infinite loop taking input from the user. Connect and disconnect both check labels 
# inputted by user to make sure labels either do not exist or exist respectively.
while True:
    inString = input('Connect, disconnect, balance, print, plot, or quit?\n')
    if inString == 'connect':
        inLabel = input('Label: ')
        inDraw = int(input('Max power draw: '))
        if deviceDict.get(inLabel) == None:
            connect(inLabel,inDraw)
        else:
            print('Error, key is taken. Please try again.')
    elif inString == 'disconnect':
        inLabel = input('Label: ')
        if deviceDict.get(inLabel) != None:
            disconnect(inLabel)
        else:
            print('Error, device does not exist. Please try again.')
    elif inString == 'balance':
        balance()
    elif inString == 'print':
        print("Available power: " + str(poolAvail))
        print(deviceDict)
    elif inString == 'plot':
        plotPower()
    elif inString == 'quit':
        break
    else:
        print('Invalid statement. Try again.')





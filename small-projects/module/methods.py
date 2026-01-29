import items
devicesArr=items.devices
def deviceAdd(deviceName,devicePrice):
     
     devicesArr[deviceName]=devicePrice

def deviceUpdate(deviceName,devicePrice):
    if deviceName in devicesArr:
        devicesArr[deviceName]=devicePrice
    else:
        print(f"There is no >>>>{deviceName}<<<< wtf are u talk about are u idiot?")

def deviceGet():
    print(devicesArr)


    
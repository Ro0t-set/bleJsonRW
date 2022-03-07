from  ble.bleConnection import BleConnection
import asyncio
#30:ae:a4:97:9f:32

def printData(mes):
    print(mes)


esp32 = BleConnection("30:ae:a4:97:9f:32", printData)



print("test")
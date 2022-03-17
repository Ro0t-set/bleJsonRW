from  ble.bleConnection import BleConnection
import asyncio
#30:ae:a4:97:9f:32

def printData(mes):
    print(mes)


esp32 = BleConnection("f0:08:d1:cc:dd:9e", printData)
esp32.whrite("ciao espppp")

print("test")
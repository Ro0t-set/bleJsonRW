from  ble.bleConnection import BleConnection
import time

def printData(mes):
    print(mes)

esp32 = BleConnection("f0:08:d1:cc:dd:9e", printData)

while True:
    print(esp32.write("ciao, sono rasp"))
    time.sleep(2)



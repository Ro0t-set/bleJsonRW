# bleJsonRW



# Scan device
utility/scan.py to to scan the bluetooth device

# BleConnection 


BleConnection object take as the first argument the mac address of the device with which we want to connect, and as second argument a function that is run when is receive a notification

Example use:

```python
from  ble.bleConnection import BleConnection
import time

def printData(mes):
    print(mes)

esp32 = BleConnection("f0:08:d1:cc:dd:9e", printData)

while True:
    print(esp32.write("Hello Word!!"))
    time.sleep(2)


```

In this example, when arrive a notification from device "f0:08:d1:cc:dd:9e", the notification will be printed 

BleConnection run a thread to maintain connection with the device

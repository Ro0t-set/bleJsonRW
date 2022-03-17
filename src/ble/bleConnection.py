from email import message
from bluepy import btle
import threading
import time
message = "FiresMessage"

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
        global message
        message =  data 
  

        # ... perhaps check cHandle
        # ... process 'data'

# Initialisation  -------


class BleConnection:
    def __init__(self, mac_addres, on_message_receive):
        self.p = btle.Peripheral(mac_addres,btle.ADDR_TYPE_PUBLIC)  
        self.on_message_receive = on_message_receive
        # Setup to turn notifications on, e.g.
        self.svc = self.p.getServiceByUUID(0xec00)
        self.ch_Tx = self.svc.getCharacteristics(0xec0e)[0]
        self.ch_Rx = self.svc.getCharacteristics(0xec0e)[0]

        self.p.setDelegate(MyDelegate())
        self.p.setMTU(512)
        self.setup_data = b"\x01\00"
        self.p.writeCharacteristic(self.ch_Rx.valHandle+1, self.setup_data)

        self.notification_thread = threading.Thread(target=self.get_notification)
        self.notification_thread.start()
 



    def get_notification(self):
        global message
        while True:
            try:
                if self.p.waitForNotifications(1.0):
                    self.on_message_receive(message)
            except:
                time.sleep(0.2)

        
    def whrite(self, message):
            btime = bytes(message , 'utf-8')
            try:        
                return self.ch_Tx.write(btime, True)

            except btle.BTLEException:
                return "btle.BTLEException"

        
    # Perhaps do something else here
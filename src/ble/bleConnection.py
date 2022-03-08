from bluepy import btle
import threading

message = ""


class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handle_notification(self, data):
        global message
        message = data


class BleConnection:
    def __init__(self, mac_address, on_message_receive):
        self.p = btle.Peripheral(mac_address, btle.ADDR_TYPE_PUBLIC)
        self.on_message_receive = on_message_receive
        # Setup to turn notifications on, e.g.
        self.svc = self.p.getServiceByUUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
        self.ch_Tx = self.svc.getCharacteristics("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")[0]
        self.ch_Rx = self.svc.getCharacteristics("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")[0]

        self.p.setDelegate(MyDelegate())
        self.p.setMTU(512)
        self.setup_data = b"\x01\00"
        self.p.writeCharacteristic(self.ch_Rx.valHandle + 1, self.setup_data)

        self.notification_thread = threading.Thread(target=self.get_notification)
        self.notification_thread.start()

    def get_notification(self):
        global message
        while True:
            if self.p.waitForNotifications(1.0):
                self.on_message_receive(message)

    def send_notification(self, message_to_send):
        str_message_to_bytes = bytes(message_to_send, 'utf-8')
        try:
            return self.ch_Tx.write(str_message_to_bytes, True)

        except btle.BTLEException:
            return "btle.BTLEException"



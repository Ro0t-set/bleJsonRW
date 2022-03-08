import time
import socket
from src.server.udp_server import serverUDP
from src.structure.sensors_data_manager import SensorDataList
import threading

# data
sensor_list = SensorDataList()
server = serverUDP("127.0.0.1", 7070)


# server
def runserver():
    for i in range(0, 10):
        sensor_list.add_sensor("temp", 20 + i)
        sensor_list.add_sensor("hum", 36 + i)
        server.update_message(sensor_list.get_json())
        time.sleep(2)


notification_thread = threading.Thread(target=runserver)
notification_thread.start()

# Client



msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("127.0.0.1", 7070)

bufferSize = 1024


for i in range(0, 10):
    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    msg = "Message from Server {}".format(msgFromServer[0])

    print(msg)
    
    time.sleep(1)

notification_thread.join()

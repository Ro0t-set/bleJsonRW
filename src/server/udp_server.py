import socketserver
import threading

class serverUDP:
    message = ''

    class MyUDPHandler(socketserver.DatagramRequestHandler):

        def handle(self):
            self.wfile.write(serverUDP.message.encode())

    def __init__(self, server_ip, server_port):
        self.server_port = server_port
        self.server_IP = server_ip
        self.serverAddress = (server_ip, server_port)
        self.serverUDP = socketserver.UDPServer(self.serverAddress, self.MyUDPHandler)

        self.notification_thread = threading.Thread(target=self.serverUDP.serve_forever)
        self.notification_thread.start()

    def update_message(self, message):
        serverUDP.message = message


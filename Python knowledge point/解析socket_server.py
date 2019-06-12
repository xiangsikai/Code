# by luffycity.com
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.request
        self.client_address
        self.server
        # 编写代码

server = socketserver.ThreadingTCPServer(('192.168.13.84',8001,),MyServer)
"""
server.server_address = server_address
server.RequestHandlerClass = RequestHandlerClass
server.__is_shut_down = threading.Event()
server.__shutdown_request = False
server.socket = socket....
    - socket.bind
    - socket.listen
"""


server.serve_forever()
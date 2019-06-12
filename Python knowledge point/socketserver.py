# by luffycity.com
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        pass

server = socketserver.ThreadingTCPServer(('192.168.13.84',8001,),MyServer)
server.serve_forever()
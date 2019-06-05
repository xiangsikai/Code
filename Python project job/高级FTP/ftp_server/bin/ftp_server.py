import os,sys
bin_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(bin_path)
from core import main
if __name__ == "__main__":
    HOST, PORT = "localhost", 9990
    server = main.socketserver.ThreadingTCPServer((HOST, PORT), main.MyTCPHandler)
    server.serve_forever()
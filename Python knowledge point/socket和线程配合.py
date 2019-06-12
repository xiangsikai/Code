# by luffycity.com
import time
import socket
import threading

def task(conn):
    time.sleep(20)
    data = conn.recv(1024)
    print(data)
    conn.close()


server = socket.socket()
server.bind(('192.168.13.84',8001,))
server.listen(5)

while True:
    conn,addr = server.accept()
    t = threading.Thread(target=task,args=(conn,))
    t.start()
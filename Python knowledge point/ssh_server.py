# by luffycity.com

import socket
import subprocess

server = socket.socket()

server.bind(('127.0.0.1',8008))

server.listen(5)

while True:
    print("server is working.....")
    conn,addr = server.accept()
    # 字节类型
    while True:
        # 针对window系统
        try:
            cmd = conn.recv(1024).decode("utf8") # 阻塞

            if cmd == b'exit':
                break

            res=subprocess.Popen(cmd,
                             shell=True,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             )
            # print("stdout",res.stdout.read())
            # print("stderr",res.stderr.read().decode("gbk"))
            out=res.stdout.read()
            err=res.stderr.read()

            print("out响应长度",len(out))
            print("err响应长度",len(err))
            if err:
                 import struct
                 header_pack = struct.pack("i", len(err))
                 conn.send(header_pack)
                 conn.send(err)
            else:
                 #构建报头
                 import struct
                 header_pack=struct.pack("i",len(out))
                 print("header_pack",header_pack)
                 # # 发送报头
                 conn.send(str(len(out)).encode("utf8"))
                 # 发送数据
                 conn.send(out)




        except Exception as e:
            break


    conn.close()
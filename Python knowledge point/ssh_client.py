import socket
import struct
sk = socket.socket()

sk.connect(('127.0.0.1',8008))

while 1:
    cmd = input("请输入命令：")
    sk.send(cmd.encode('utf-8')) # 字节
    if cmd=="":
        continue
    if cmd == 'exit':
        break

    # header_pack=sk.recv(4)
    # data_length=struct.unpack("i",header_pack)[0]
    # print("data_length",data_length)
    '''
    b'xxx/xxx/xxx/bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
    
    
    '''
    data_length=int(sk.recv(1024).decode("utf8"))
    print("data_length",data_length)

    recv_data_length=0
    recv_data=b""

    while recv_data_length<data_length:
        data=sk.recv(1024)
        recv_data_length+=len(data)
        recv_data+=data

    print(recv_data.decode("gbk"))


sk.close()

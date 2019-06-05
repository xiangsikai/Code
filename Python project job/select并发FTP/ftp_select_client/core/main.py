import socket,os,pickle,time

class FTP_Client():
    """client类"""
    def __init__(self):
        self.client = socket.socket()

    def ftp_clint(self):
        self.client.connect(('localhost',9900))
        print("并发FTP 上传/下载\n"
              "下载:get filename\n"
              "上传:put filename\n")
        while True:
            cmd = input(">>:").strip()
            if len(cmd) == 0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,cmd_str):
                func = getattr(self,cmd_str)
                func(cmd)
            else:
                print("输入指令有误")

    def put(self,*args):
        filename = args[0].split()[1]
        filesize = os.stat(filename).st_size
        if os.path.isfile(filename):
                msg_dic = {
                    "action":"put",
                    "filename":filename,
                    "filesize":filesize,
                    "size":None,
                    "judeg":True,
                    }
                #　序列化字典发送服务端
                self.client.send(pickle.dumps(msg_dic))
                ack1 = self.client.recv(1024)
                size = 0
                file_name = open(filename,"rb")
                for line in file_name:
                    size = len(line)
                    msg_dic["size"] = int(size)
                    self.client.send(line)

                else:
                    print("OK")
        else:
            print("文件不存在")

    def get(self,*args):
        filename = args[0].split()[1]
        if not os.path.isfile(filename):
            msg_dic = {
                    "action":"get",
                    "filename":filename,
                    "filesize":None,
                    "size":None,
                    "judeg":True,
                    }
            #　序列化字典发送服务端
            self.client.send(pickle.dumps(msg_dic))
            ack = self.client.recv(1024)
            self.client.send(b"ok")
            filesize = self.client.recv(1024)
            time.sleep(0.001)
            filesize = int(filesize.decode())
            num = 0
            size = 0
            file_name = open(filename,"wb")
            while num < filesize:
                if filesize - num > 1024:
                    size = 1024
                    ack2 = self.client.send(b"ok")
                    data = self.client.recv(size)
                    file_name.write(data)
                    num += len(data)
                else:
                    size = filesize - num
                    ack2 = self.client.send(b"ok")
                    data = self.client.recv(size)
                    file_name.write(data)
                    num += len(data)
            else:
                print("OK")
        else:
            print("该文件已存在")



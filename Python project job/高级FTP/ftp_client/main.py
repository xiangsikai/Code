import socket,os,json,hashlib,sys,base64,pickle

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    # 交互
    def interactive(self):
        self.authenticate()
        self.client.send(b"ok")
        path = self.client.recv(1024)
        self.path = path.decode()
        self.directory_list = []
        self.directory = ""
        self.help()
        while True:
            cmd = input("[%s@localhost %s%s]$ "%(self.username,self.path,self.directory)).strip()
            if len(cmd) == 0:continue
            # 切割命令符
            if cmd == "ls":
                self.cmd_ls()
                continue
            cmd_str = cmd.split()[0]
            # 反射命令
            if hasattr(self,"cmd_%s"%(cmd_str)):
                func = getattr(self,"cmd_%s"%(cmd_str))
                func(cmd)
            else:
                self.help()

    # 帮助
    def help(self):
        msg ='''
            ls              | 查看当前目录文件
            cd ..           | 返回上级目录
            cd directory\   | 进入下级目录
            get filename    | 下载文件
            put filename    | 上传文件
            '''
        print(msg)

    # 连接
    def connect(self,ip,port):
        self.client.connect((ip,port))

    # 上传
    def cmd_put(self,*args):
        # 取出cmd
        cmd_split = args[0].split()
        if len(cmd_split) >1:
            # 切割文件名
            filename = cmd_split[1]
            # 判断文件是否存在
            if os.path.isfile(filename):
                # 赋值文件大小
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action":"put",
                    "filename":filename,
                    "size":filesize,
                    "file_to":False,
                    "ovrttiffrn":True,}
                #　序列化字典发送服务端
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                conn_dic = self.client.recv(1024)
                conn_dic = pickle.loads(conn_dic)
                if not conn_dic["file_to"]:
                    # 防止粘包，服务器确认，做标准返回
                    server_response = self.client.recv(1024)
                    # md5加密
                    with open(filename,"rb") as filemd5:
                        md5c = hashlib.md5()
                        md5c.update(filemd5.read())
                        md5 = md5c.hexdigest()
                    # 进度条递增数据大小
                    num_size = 0
                    int = 0
                    pro_size = filesize / 101
                    f = open(filename,"rb")
                    # 循环发送服务端上传文件
                    for line in f:
                            self.client.send(line)
                            data = len(line)
                            num_size += data
                            flag_disk = self.client.recv(1024)
                            if str(flag_disk.decode()) == "no":
                                print("\n\033[31;1m用户存储以达上限..\033[0m")
                                exit()
                            if num_size > pro_size:
                                num_size = 0
                                int += 1
                                self.progressbar(int)
                                continue
                    # 返回md5校验
                    server_md5 = self.client.recv(1024)
                    self.client.send(md5.encode("utf-8"))
                    print("\n服务端MD5:%s\n客户端MD5:%s"%(md5,server_md5.decode()))
                    print("文件[%s]上传成功"%filename)
                    f.close()
                else:
                    self.client.send(b"ok")
                    # 文件总大小
                    file_size_1 = conn_dic["size"]
                    # 上次上传的文件大小
                    file_size_2 = conn_dic["size_to"]
                    # 需要传输大小
                    file_size_3 = file_size_1 - file_size_2
                    int = 0
                    num_size = 0
                    pro_size = file_size_3 / 101
                    with open(filename,"rb") as file_name:
                        file_name.seek(file_size_2)
                        for line in file_name:
                            self.client.send(line)
                            data = len(line)
                            num_size += data
                            flag_disk = self.client.recv(1024)
                            if str(flag_disk.decode()) == "no":
                                print("\n\033[31;1m用户存储以达上限..\033[0m")
                                exit()
                            if num_size > pro_size:
                                num_size = 0
                                int += 1
                            self.progressbar(int)
                        else:
                            print("\n续上传完成！！")
        else:
            print("输入错误")

    # 下载
    def cmd_get(self,*args):
        # 取出cmd
        cmd_split = args[0].split()
        if len(cmd_split) >1:
            filename = cmd_split[1]
            if not os.path.isfile(filename):
                msg_dic = {
                    "action":"get",
                    "filename":filename,
                    "size":None,
                    "file_to":False,
                    "ovrttiffrn":True
                }
                # 发送字典
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                # 接收字典
                conn_dic = self.client.recv(1024)
                conn_dic = json.loads(conn_dic.decode())
                filesize = conn_dic["size"]
                # 防止粘包，服务器确认，做标准返回
                self.client.send(b"ok")
                # 进度条测试文件大小
                # 递增文件大小
                num_size = 0
                received_size = 0
                # 每次下载字节大小
                size = 0
                # 递增接收MD5加密内容
                md5_str = []
                pro_size_num = filesize / 99
                num_size = 0
                int = 0
                f_get = open(filename,"wb")
                while received_size < filesize:
                    # 判断是否是最后一次
                    if filesize - received_size > 1024:
                        size = 1024
                        data = self.client.recv(size)
                        f_get.write(data)
                        received_size += len(data)
                        num_size += len(data)
                        md5_str.append(data)
                        # 进度条
                        if num_size > pro_size_num:
                            num_size = 0
                            int = int + 1
                            self.progressbar(int)
                    else:
                        # 接收最后一次
                        size = filesize - received_size
                        data = self.client.recv(size)
                        f_get.write(data)
                        received_size += len(data)
                        md5_str.append(data)
                        int = int + 1
                        self.progressbar(int)
                else:
                    f_get.close()
                    # 调用MD5
                    with open(filename,"rb") as md5c:
                        client_md5 = hashlib.md5()
                        for line in md5c:
                            client_md5.update(line)
                        md5 = client_md5.hexdigest()
                        self.client.send(md5.encode("utf-8"))
                        server_md5 = self.client.recv(1024)
                    print("\n服务端MD5:%s\n客户端MD5:%s"%(md5,server_md5.decode()))
                    print("文件[%s]下载完成！"%filename)
            else:
                msg_dic = {
                    "action":"get",
                    "filename":filename,
                    "size":None,
                    "size_to":None,
                    "file_max":None,
                    "file_to":True,
                    "ovrttiffrn":True
                }
                # 已传传输大小
                filesize = os.stat(filename).st_size
                msg_dic["size"] = filesize
                # 发送字典
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                conn_dic = self.client.recv(1024)
                conn_dic = json.loads(conn_dic.decode())
                # 需要下载的大小
                filesize3 = conn_dic["size_to"]
                file_max = conn_dic["file_max"]
                self.client.send(b"ok")
                # 传入文件大小
                re_size = 0
                re_size2 = 0
                # recv大小
                size = 0
                pro_size_num = filesize3 / 101
                num_size = 0
                int = 0
                # 打开文件
                with open(filename,'ba+') as file_to:
                    while True:
                            size = 1024
                            data_to = self.client.recv(size)
                            file_to.write(data_to)
                            re_size += size
                            num_size += len(data_to)
                            re_size2 += len(data_to)
                            if num_size > pro_size_num:
                                num_size = 0
                                int = int + 1
                                self.progressbar(int)
                            if re_size2 >= filesize3:
                                print("\n续下载完成！")
                                break
        else:
           print("请输入正确指令\n%s"%self.help())

    # 目录切换
    def cmd_cd(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) >1:
            # 切割文件名
            cd_path = cmd_split[1]
            msg_dic = {
                "action":"cd",
                "filename":cd_path,
                "directory":False,
                "ovrttiffrn":True,
            }
            #　序列化字典发送服务端
            self.client.send(json.dumps(msg_dic).encode("utf-8"))
            if cd_path == "..":
                try:
                    self.directory_list.pop()
                except IndexError as e:
                    print("只能在home目录内活动")
                if len(self.directory_list) == 0:
                    self.directory = ""
                else:
                    self.directory = ""
                    for dire in self.directory_list:
                        self.directory += dire
            else:
                self.directory = ""
                cd_dict = self.client.recv(1024)
                cd_dict = json.loads(cd_dict)
                if cd_dict["directory"]:
                    self.directory_list.append(cd_path)
                    for dire in self.directory_list:
                        self.directory += dire
                else:
                    print("无访问目录")

    # 查看当前目录下文件
    def cmd_ls(self):
            msg_dic = {
                "action":"ls",
                "filename":None,
                "ls":False,
                "ovrttiffrn":True,
            }
            #　序列化字典发送服务端
            self.client.send(json.dumps(msg_dic).encode("utf-8"))
            data = self.client.recv(1024)
            data = json.loads(data.decode())
            print("\n当前目录下:")
            for line in data:
                print("-- %s --"%line)

    # 验证用户登陆
    def authenticate(self):
        login_dict = {"user":None,"pass":None,}
        print("<╋ FTP登陆 ╋>\n")
        flag = True
        while flag:
            username = input("_login>>:").strip()
            password = input("_password>>:").strip()
            self.username = username
            login_dict["user"] = base64.encodestring(username.encode("utf-8"))
            login_dict["pass"] = base64.encodestring(password.encode("utf-8"))
            login_dict["flag"] = False
            self.client.send(pickle.dumps(login_dict))
            login_dict = self.client.recv(1024)
            login_dict = pickle.loads(login_dict)
            if login_dict["flag"]:
                flag = False
                print("[%s]登陆成功.."%username)
                self.client.send(b"ok")
            else:
                print("用户名或密码错误..\n")
        else:
            disk_max = self.client.recv(1024)
            self.client.send(b"ok")
            disk_num = self.client.recv(1024)
            print("用户存储:[%s字节]\n已用存储:[%s字节]"%(disk_max.decode(),disk_num.decode()))

    # 进度条
    def progressbar(self,int):
        percent = ("%s%%"%int)
        sys.stdout.write("\r[%-100s]%s"%(">" * int,percent))
        sys.stdout.flush()




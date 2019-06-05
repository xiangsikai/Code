import socketserver,json,os,hashlib,sys,base64,pickle
main_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_path)

from conf import path

class MyTCPHandler(socketserver.BaseRequestHandler):

    # 上传
    def put(self,*args):
        """接收客户端文件"""
        # 取出cmd
        cmd_dic = args[0]
        # 获取文件
        filename = cmd_dic["filename"]
        # 获取文件大小
        filesize_max = cmd_dic["size"]
        self.filesize_max = filesize_max
        # 判断文件是否存在
        if os.path.isfile("%s%s"%(self.dir,filename)):
            filesize = os.stat("%s%s"%(self.dir,filename)).st_size
            cmd_dic["size_to"] = int(filesize)
            cmd_dic["file_to"] = True
            self.request.send(json.dumps(cmd_dic).encode("utf-8"))
            # 文件总大小
            filesize1 = cmd_dic["size"]
            self.filesize_max = filesize1
            # 上次收已收大小
            filesize2 = cmd_dic["size_to"]
            # 需要接收数据大小
            filesize3 = filesize1 - filesize2
            ack = self.request.recv(1024)
            # 递增接收数据大小
            size_to = 0
            # recv大小
            size = 0
            with open("%s%s"%(self.dir,filename),"ba+") as file_name:
                while size_to < self.filesize_max:
                    size = 1024
                    data_to = self.request.recv(size)
                    file_name.write(data_to)
                    size_to += len(data_to)
                    # 递增磁盘配额
                    self.disk_quta_num += len(data_to)
                    # 判断用户磁盘
                    self.disk_qutaa_judge()
                    if filesize3 <= size_to:
                        print("续上传完成!")
                        break
        else:
            self.request.send(pickle.dumps(cmd_dic))
            # 不存在就写入文件
            f = open("%s%s"%(self.dir,filename),"wb")
            # ACK返回确认
            self.request.send(b"ok")
            # 递增接收文件大小
            received_size = 0
            # 接收字节
            size = 0
            # 建立md5
            md5_str = []
            md5s = hashlib.md5()
            # 传入数据比总数据小就成立
            while received_size < self.filesize_max:
                if self.filesize_max - received_size > 1024:
                    size = 1024
                    data = self.request.recv(size)
                    f.write(data)
                    received_size += len(data)
                    # 递增磁盘配额
                    self.disk_quta_num += len(data)
                    md5_str.append(data)
                    # 判断用户磁盘
                    self.disk_qutaa_judge()
                else:
                    size = self.filesize_max - received_size
                    data = self.request.recv(size)
                    f.write(data)
                    received_size += len(data)
                    self.disk_quta_num += len(data)
                    md5_str.append(data)
                    self.disk_qutaa_judge()
            else:
                f.close()
                for line in md5_str:
                    md5s.update(line)
                md5 = md5s.hexdigest()
                md5 = str(md5).encode("utf-8")
                self.request.send(md5)
                clint_md5 = self.request.recv(1024)
                if md5 == clint_md5:
                    print("上传[%s]OK！."%filename)
                else:
                    print("文件不完正")

    # 下载
    def get(self,*args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        if os.path.isfile("%s%s"%(self.dir,filename)):
            if not cmd_dic["file_to"]:
                filesize = os.stat("%s%s"%(self.dir,filename)).st_size
                cmd_dic["size"] = filesize
                self.request.send(json.dumps(cmd_dic).encode("utf-8"))
                # 防止粘包
                client_response = self.request.recv(1024)
                # 打开文件
                f_get = open("%s%s"%(self.dir,filename),"rb")
                for line in f_get:
                    self.request.send(line)
                else:
                    f_get.close()
                # 调用MD5
                with open("%s%s"%(self.dir,filename),"rb") as md5s:
                    server_md5 = hashlib.md5()
                    server_md5.update(md5s.read())
                    md5 = server_md5.hexdigest()
                client_md5 = self.request.recv(1024)
                self.request.send(md5.encode("utf-8"))
                client_md5 = client_md5.decode()
                if md5 == client_md5:
                    print("[%s]OK!"%filename)
                else:
                    print("[%s]文件不完整！"%filename)
            else:
                # 上次传输的文件大小
                filesize1 = cmd_dic["size"]
                # 文件总大小
                filesize2 = os.stat("%s%s"%(self.dir,filename)).st_size
                # 没有传输的文件大小
                filesize3 = int(filesize2) - int(filesize1)
                cmd_dic["size_to"] = int(filesize3)
                cmd_dic["file_max"] = int(filesize2)
                self.request.send(json.dumps(cmd_dic).encode("utf-8"))
                # 防止粘包
                client_ack = self.request.recv(1024)
                # 递增数据
                # file_size_to = 0
                # 读取文件
                file = open("%s%s"%(self.dir,filename),"rb")
                file.seek(int(filesize1))
                for line in file:
                    self.request.send(line)
                else:
                    print("续传[%s]文件完成"%filename)
                    print("断点传送大小:%s"%filesize3)
        else:
            print("无本地文件")

    # 切换目录
    def cd(self,*args):
         # 取出cmd
        cmd_dic = args[0]
        # 获取目录路径
        cd_path = cmd_dic["filename"]
        # 判断目录是否存在
        if cd_path == "..":
            self.dir2 = self.dir3
            try:
                self.dir_sion.pop()
            except IndexError as e:
                print("只能在home目录内活动")
            if len(self.dir_sion) == 0:
                self.dir = self.dir3
            else:
                for dire in self.dir_sion:
                    self.dir2 += dire
                self.dir = self.dir2
            print(self.dir)
        else:
            if os.path.isdir("%s%s"%(self.dir,cd_path)):
                self.dir2 = self.dir3
                self.dir_sion.append(cd_path)
                for dire in self.dir_sion:
                    self.dir2 += dire
                self.dir = self.dir2
                cmd_dic["directory"] = True
                self.request.send(json.dumps(cmd_dic).encode("utf-8"))
            else:
                self.request.send(json.dumps(cmd_dic).encode("utf-8"))
            print(self.dir)

    # 查看目录
    def ls(self,*args):
       # 取出cmd
        cmd_dic = args[0]
        data = os.listdir("%s"%(self.dir))
        self.request.send(json.dumps(data).encode("utf-8"))

    # 磁盘配额限制
    def disk_quota_limit(self):
        print("\n--新用户[%s]--磁盘配额--输入字节--"%self.name)
        flag = True
        while flag:
            num = input(">>:").strip()
            if not num.isdigit():
                print("必须是整数字-!")
            else:
                disk_file = open("%s%s_disk_max"%(path.data_path,self.name),"w")
                disk_file.write(num)
                disk_file.close()
                flag = False
                self.flag =False

    # 磁盘配额增加
    def disk_qutaa_add(self):
        num = 0
        if os.path.isfile("%s%s_disk_num"%(path.data_path,self.name)):
            with open("%s%s_disk_num"%(path.data_path,self.name)) as disk_max:
                num = disk_max.read()
            num_max = int(num) + self.disk_quta_num
            with open("%s%s_disk_num"%(path.data_path,self.name),"w") as disk_num:
                disk_num.write(str(num_max))
        else:
            print("无磁盘使用文件！")

    # 创建磁盘配额文件
    def disk_qutaa_file(self):
        if not os.path.isfile("%s%s_disk_num"%(path.data_path,self.name)):
            with open("%s%s_disk_num"%(path.data_path,self.name),"w") as disk_max:
                disk_max.write(str(self.disk_quta_num))

    # 磁盘配额判断
    def disk_qutaa_judge(self):
        if int(self.disk_quta_max) < int(self.disk_quta_num):
            print("\033[31;1m用户[%s]存储以达上限..\033[0m"%self.name)
            self.filesize_max = 0
            self.request.send(b"no")
        else:
            self.request.send(b"yes")

    # 磁盘配额取值
    def disk_qutaa_value(self):
        with open("%s%s_disk_num"%(path.data_path,self.name)) as disk_value:
            data = disk_value.read()
            self.disk_quta_num = int(data)

    # 用户登陆
    def authenticate(self,):
        flag = True
        while flag:
            login_dict = self.request.recv(1024)
            login_dict = pickle.loads(login_dict)
            username = base64.decodestring(login_dict["user"])
            password = base64.decodestring(login_dict["pass"])
            username = username.decode()
            password = password.decode()
            login_file = open(path.data_path + "login_user")
            for line in login_file:
                if line == "\n":continue
                login_user,login_pass = line.split(",")
                login_pass = login_pass.strip("\n")
                if login_user == username and login_pass == password:
                    login_dict["flag"] = True
            else:
                self.request.send(pickle.dumps(login_dict))
                if login_dict["flag"]:
                    self.name = username
                    print("[%s] 已登录.."%username)
                    flag = False
                else:
                    print("{} 登陆失败:".format(self.client_address[0]))

    # 交互
    def handle(self,):
        # 上级目录
        self.dir_sion = []
        # 登陆用户
        self.name = ""
        # 存储使用大小
        self.disk_quta_num = 0
        # 存储限制大小
        self.disk_quta_max = 0
        self.authenticate()
        # 磁盘配额，创建 家目录
        self.flag = True
        while self.flag:
            if not os.path.isdir(path.data_path + "%s_home\\"%self.name):
                os.mkdir(path.data_path + "%s_home\\"%self.name)
                self.disk_quota_limit()
            else:
                self.flag = False
        with open("%s%s_disk_max"%(path.data_path,self.name)) as disk_max:
            self.disk_quta_max = disk_max.read()
        ack1 = self.request.recv(1024)
        self.request.send(str(self.disk_quta_max).encode("utf-8"))
        # 用户home绝对路径
        self.dir = "%s%s_home\\"%(path.data_path,self.name)
        self.dir2 = "%s%s_home\\"%(path.data_path,self.name)
        self.dir3 = "%s%s_home\\"%(path.data_path,self.name)
        # client终端路径
        self.path = "%s_home\\"%(self.name)
        self.disk_qutaa_file()
        self.disk_qutaa_value()
        ack2 = self.request.recv(1024)
        self.request.send(str(self.disk_quta_num).encode("utf-8"))
        ack3 = self.request.recv(1024)
        self.request.send(str(self.path).encode("utf-8"))
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)
            except ConnectionResetError as e:
                print("err",e)
                self.disk_qutaa_add()
                break
            except ConnectionAbortedError as ee:
                print("文件传输时断开链接..",ee)
                self.disk_qutaa_add()
                break



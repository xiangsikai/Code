import select
import socket
import queue
import pickle
import os
import time

class Select_ftp(object):
    """select类"""
    def __init__(self):
        # 指定socket协议
        self.server = socket.socket()
        # 队列字典
        self.msg_dic = {}
        # 接收客户链接列表
        self.inputs = [self.server,]
        # 接收客户数据列表
        self.outputs = []
        # 链接数据字典
        self.dic = {}
        self.num = 0

    def socket_interaction(self):
        """socket传入参数"""
        self.server.bind(('localhost', 9900))
        self.server.listen(10000)
        self.server.setblocking(False)

    def action_select(self):
        """等待Client端请求"""
        # 开启socket监听
        self.socket_interaction()
        while True:
            # select 有链接数据就返回所有链接循环，无链接数据就等待请求。
            self.readable,self.writeables,self.exceptional = select.select(self.inputs,self.outputs,self.inputs)
            # 接收链接
            self.closed()
            # 收发数据
            self.write_data()
            # 删除链接
            self.del_link()

    def closed(self):
        """注册链接Client端 """
        for link in self.readable:
            if link is self.server:
                # 等待客户端生成实例
                conn,addr = self.server.accept()
                self.dic[conn] = {
                    "filename":None,        # 文件名
                    "filesize":0,           # 文件大小
                    "action":None,          # 动作方法
                    "judge":True,           # 判断首次链接
                    "tran":True,            # 判断下载交互
                    "receive_size":0,       # 已接收文件大小
                    }
                # 打印客户端IP地址
                print("来了个新连接",addr)
                # 将新连接添加到客户端链接列表
                self.inputs.append(conn)
                # 初始化一个队列，后面存要返回这个客户端的数据
                self.msg_dic[conn] = queue.Queue()
            else:
                # 获取数据
                data = link.recv(1024)
                # 将返回的数据排列到队列中
                self.msg_dic[link].put(data)
                # 放入返回的链接队列
                self.outputs.append(link)

    def write_data(self):
        """发数据要返回给客户端的链接列表"""
        for conn in self.writeables:
            # 重链接列表中取出队列的实例
            try:
                if self.dic[conn]["judge"]:
                    data_dict = self.msg_dic[conn].get()
                    data_dict = pickle.loads(data_dict)
                    self.dic[conn]["filename"] = data_dict["filename"]
                    self.dic[conn]["filesize"] = data_dict["filesize"]
                    self.dic[conn]["action"] = data_dict["action"]
                    self.dic[conn]["judge"] = False
                    conn.send(b"ok")
                    # 确保下次循环的时候writeable，不返回这个已经处理完的链接
                    self.outputs.remove(conn)
                    break
                else:
                    if hasattr(self,self.dic[conn]["action"]):
                        func = getattr(self,self.dic[conn]["action"])
                        func(conn)
                    else:
                        print("执行方法错误")
            except Exception as e:
                break

    def put(self,conn):
        """上传"""
        if os.path.isfile("num_%s"%self.dic[conn]["filename"]):
            with open("num_%s"%self.dic[conn]["filename"]) as num_file2:
                self.num = int(num_file2.read())
        file_name = open(self.dic[conn]["filename"],"a+b")
        if int(self.num) < int(self.dic[conn]["filesize"]):
            self.data = self.msg_dic[conn].get()
            file_name.write(self.data)
            self.num = len(self.data)
            if not os.path.isfile("num_%s"%self.dic[conn]["filename"]):
                with open("num_%s"%self.dic[conn]["filename"],"w") as num_file1:
                    num_file1.write(str(self.num))
            else:
                with open("num_%s"%self.dic[conn]["filename"]) as num_file2:
                    self.num = int(num_file2.read()) + self.num
                with open("num_%s"%self.dic[conn]["filename"],"w") as num_file3:
                    num_file3.write(str(self.num))
            print(self.num,self.dic[conn]["filesize"])
            self.outputs.remove(conn)
            if int(self.num) == int(self.dic[conn]["filesize"]):
                file_name.close()
                print("OK")
                os.remove("num_%s"%self.dic[conn]["filename"])
                self.dic[conn]["judge"] = True
            self.num = 0

    def get(self,conn):
        """下载"""
        if self.dic[conn]["tran"]:
            self.data = self.msg_dic[conn].get()
            filesize = os.stat(self.dic[conn]["filename"]).st_size
            self.dic[conn]["filesize"] = filesize
            conn.send(str(filesize).encode("utf-8"))
            self.dic[conn]["tran"] = False
            self.outputs.remove(conn)
        else:
            self.data = self.msg_dic[conn].get()
            file_name = open(self.dic[conn]["filename"],"rb")
            file_name.seek(self.dic[conn]["receive_size"])
            receive_size = 0
            size_num = 0
            for line in file_name:
                conn.send(line)
                receive_size += len(line)
                size_num += 1
                if size_num == 10:
                    size_num = 0
                    break
            self.outputs.remove(conn)
            self.dic[conn]["receive_size"] = self.dic[conn]["receive_size"] + receive_size
            send_num = 0
            print(self.dic[conn]["receive_size"], self.dic[conn]["filesize"])
            if self.dic[conn]["receive_size"] == self.dic[conn]["filesize"]:
                self.dic[conn]["tran"] = True
                self.dic[conn]["judge"] = True
                file_name.close()
                print("OK")

    def del_link(self):
        """删除链接Clinet"""
        # 删除：错误链接
        for delete in self.exceptional:
            # 查找错误链接是否存在outputs
            if delete in self.outputs:
                # 如果有就删除错误链接
                self.outputs.remove(delete)
            # 删除inputs下的错误链接
            self.inputs.remove(delete)
            # 删除队列中的错误链接
            del self.msg_dic[delete]
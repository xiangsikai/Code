# by luffycity.com

# python
# 序列化 : 字符串 bytes
# 序列 : 列表 元组 字符串 bytes

# 把其他的数据类型 转换成 字符串 bytes  序列化的过程

# str
# dic = {'1':'2'}
# print([str(dic),dic])
# print([str([1,2,3]),[1,2,3]])

# 为什么要把其他数据类型转换成字符串???
# 能够在网络上传输的只能是bytes,
# 能够存储在文件里的只有bytes和str
# dic = {'小明':{'phone_num':123123123123,}}
# '''
# 小明|电话|性别
# 小张|...
# '''
# 字典 -> 字符串 -通过网络去传输-> 字符串 -> 字典

# 转字符串的过程 不就是数据类型的强制转换么?为什么要学个序列化模块?
# 字符串 -> 字典
# str_dic = str([1,2,3])
# print(str_dic,type(str_dic))


# 文件中读出来的 网络上接收来的
# res = eval(str_dic)
# print(res,type(res))

# eval 要谨慎的使用,用户的输入/网络上接收的数据/文件中的内容
# eval('import os;os.remove('c:')')
# eval('import urllib;')

# 你已知的代码 但是可能需要一些拼接 根据你自己的逻辑去做的拼接


# json
# pickle
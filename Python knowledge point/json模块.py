# by luffycity.com
# dic = {'key' : 'value','key2' : 'value2'}
# import json
# ret = json.dumps(dic)  # 序列化
# print(dic,type(dic))
# print(ret,type(ret))

# res = json.loads(ret) # 反序列化
# print(res,type(res))

# 问题1
# dic = {1 : 'value',2 : 'value2'}
# ret = json.dumps(dic)  # 序列化
# print(dic,type(dic))
# print(ret,type(ret))
#
# res = json.loads(ret) # 反序列化
# print(res,type(res))

# 问题2
# dic = {1 : [1,2,3],2 : (4,5,'aa')}
# ret = json.dumps(dic)  # 序列化
# print(dic,type(dic))
# print(ret,type(ret))

# res = json.loads(ret) # 反序列化
# print(res,type(res))

# 问题3
# s = {1,2,'aaa'}
# json.dumps(s)

# 问题4 # TypeError: keys must be a string
# json.dumps({(1,2,3):123})

# json 在所有的语言之间都通用 : json序列化的数据 在python上序列化了 那在java中也可以反序列化
# 能够处理的数据类型是非常有限的 : 字符串 列表 字典 数字
# 字典中的key只能是字符串

# 后端语言 java c c++ c#
# 前端语言 在网页上展示

# 向文件中记录字典
import json
# dic = {'key' : 'value','key2' : 'value2'}
# ret = json.dumps(dic)  # 序列化
# with open('json_file','a') as f:
#     f.write(ret)

# 从文件中读取字典
# with open('json_file','r') as f:
#     str_dic = f.read()
# dic = json.loads(str_dic)
# print(dic.keys())

# dump load 是直接操作文件的
# dic = {'key1' : 'value1','key2' : 'value2'}
# with open('json_file','a') as f:
#     json.dump(dic,f)

# with open('json_file','r') as f:
#     dic = json.load(f)
# print(dic.keys())

# 问题5 不支持连续的存 取
# dic = {'key1' : 'value1','key2' : 'value2'}
# with open('json_file','a') as f:
#     json.dump(dic,f)
#     json.dump(dic,f)
#     json.dump(dic,f)

# with open('json_file','r') as f:
#     dic = json.load(f)
# print(dic.keys())

# 需求 :就是想要把一个一个的字典放到文件中,再一个一个取出来???
# dic = {'key1' : 'value1','key2' : 'value2'}
#
# with open('json_file','a') as f:
#     str_dic = json.dumps(dic)
#     f.write(str_dic+'\n')
#     str_dic = json.dumps(dic)
#     f.write(str_dic + '\n')
#     str_dic = json.dumps(dic)
#     f.write(str_dic + '\n')

# with open('json_file','r') as f:
#     for line in f:
#         dic = json.loads(line.strip())
#         print(dic.keys())

# json
# dumps loads
    # 在内存中做数据转换 :
        # dumps 数据类型 转成 字符串 序列化
        # loads 字符串 转成 数据类型 反序列化
# dump load
    # 直接将数据类型写入文件,直接从文件中读出数据类型
        # dump 数据类型 写入 文件 序列化
        # load 文件 读出 数据类型 反序列化
# json是所有语言都通用的一种序列化格式
    # 只支持 列表 字典 字符串 数字
    # 字典的key必须是字符串


# dic = {'key':'你好'}
# print(json.dumps(dic,ensure_ascii=False))

# import json
# data = {'username':['李华','二愣子'],'sex':'male','age':16}
# json_dic2 = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=False)
# print(json_dic2)

# 存文件/传网络

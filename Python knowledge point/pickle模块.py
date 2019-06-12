# by luffycity.com
import pickle
# 支持在python中几乎所有的数据类型
dic = {(1,2,3):{'a','b'},1:'abc'}

# ret = pickle.dumps(dic)
# print(ret)
#2. dumps 序列化的结果只能是字节
# print(pickle.loads(ret))
# 3.只能在python中使用
# 4.在和文件操作的时候,需要用rb wb的模式打开文件
# 5.可以多次dump 和 多次load
# dump
# with open('pickle_file','wb') as f:
#     pickle.dump(dic,f)

# load
# with open('pickle_file','rb') as f:
#     ret = pickle.load(f)
#     print(ret,type(ret))

# dic = {(1,2,3):{'a','b'},1:'abc'}
# dic1 = {(1,2,3):{'a','b'},2:'abc'}
# dic2 = {(1,2,3):{'a','b'},3:'abc'}
# dic3 = {(1,2,3):{'a','b'},4:'abc'}
# with open('pickle_file','wb') as f:
#     pickle.dump(dic, f)
#     pickle.dump(dic1, f)
#     pickle.dump(dic2, f)
#     pickle.dump(dic3, f)

# with open('pickle_file','rb') as f:
#     ret = pickle.load(f)
#     print(ret,type(ret))
#     ret = pickle.load(f)
#     print(ret,type(ret))
#     ret = pickle.load(f)
#     print(ret, type(ret))
#     ret = pickle.load(f)
#     print(ret, type(ret))
#     ret = pickle.load(f)
#     print(ret, type(ret))

with open('pickle_file','rb') as f:
    while True:
        try:
            ret = pickle.load(f)
            print(ret,type(ret))
        except EOFError:
            break
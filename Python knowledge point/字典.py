# by luffycity.com

# dic = {'name':'alex','age':9000}   #字符串
# print(dic)
#
# dic = {1:'a',2:'b',3:'c'}           #数字
# print(dic)
#
# dic = {True:'1',False:'0'}          #布尔值
# print(dic)
#
# dic = {(1,2,3):'abc'}                #元组
# print(dic)

# dic = {[1,2,3]:'abc'}
# print(dic)


#增
    # dic['火女'] = '人头狗'   # 新增
    # # print(dic)
    # dic.setdefault('火女','安妮')     # 如果在字典中存在就不进行任何操作,不存在就进行添加
    # dic.setdefault('火女','火男')
# 删

    # ret = dic.pop('易大师')  #通过key删除  返回被删除的value
    # print(ret)
    # del dic['剑豪']
    # dic.clear()   # {}

    # ret = dic.popitem()   #随机删除  返回值 一个元组  (key,value)
    # print(ret)
    # print(dic)

# 改:
    # dic['剑豪'] = '哈莎阁'   # 强制修改

    # dic1 = {'火女':'安妮','火男':'布兰德','维恩':'暗影猎手','剑豪':'哈莎阁'}
    # dic1.update(dic)
    #
    # print(dic1)

# 查

    # for 循环       元组  键  值   键值对

    # for i in  dic:
    #     print(i)     #for 循环默认是获取字典中的键

    # print(dic['易大师父'])                   #查看1   没有这个键的时候查询会报错
    # print(dic.get('易大师','你傻啊,没有!'))    #查看2   没有返回None 可以指定返回内容

    # print(dic.setdefault('易大师范湖'))        #查看3    没有返回None


# 其他操作(字典中独特的)
    # keys  values items

    # print(dic.keys())  # (高仿列表)
    # print(dic.values())  # (高仿列表)
    # print(dic.items())
    # for i in dic.keys():
    #     print(i)
    #
    # for i in dic:
    #     print(i)     #获取到字典中的每一个键

    # for i in dic.values():
    #     print(i)     #获取到字典中的每一个值

    # for i in dic.items():
    #     print(i)


    # 解构(解包)

    # a,b = '12'   #将后边解构打开按位置赋值给变量 支持  字符串 列表 元组
    # print(a)
    # print(b)
    # dic = {'易大师':'剑圣','剑豪':'托儿所','草丛伦':'大宝剑'}
    # for a,b in dic.items():
    #     print(a)
    #     print(b)


    # dic1 = {}
    #
    # dics = dic1.fromkeys([1,2,3],'abc')


# 字典嵌套:

dic = {
    'name':'汪峰',
    'age':43,
    'wife':{
        'name':'国际章',
        'age':39,
        'salary':100000
    },
    'baby':[
        {'name':'熊大','age':18},
        {'name':'熊二','age':15},
    ]

}

dic['baby'][0]['age'] = 19

print(dic)
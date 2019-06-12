# by luffycity.com
import re
# 永远不要起一个py文件的名字 这个名字和你已知的模块同名
# regex

# 查找
# findall : 匹配所有 每一项都是列表中的一个元素
# ret = re.findall('\d+','sjkhk172按实际花费928') # 正则表达式,带匹配的字符串,flag
# ret = re.findall('\d','sjkhk172按实际花费928') # 正则表达式,带匹配的字符串,flag
# print(ret)

# search : 只匹配从左到右的第一个,得到的不是直接的结果,而是一个变量,通过这个变量的group方法来获取结果
# 如果没有匹配到,会返回None,使用group会报错
# ret = re.search('\d+','sjkhk172按实际花费928')
# print(ret)  # 内存地址,这是一个正则匹配的结果
# print(ret.group()) # 通过ret.group()获取真正的结果

# ret = re.search('\d','owghabDJLBNdgv')
# print(ret)
# print(ret.group())

# ret = re.search('\d+','sjkhk172按实际花费928')
# if ret :   # 内存地址,这是一个正则匹配的结果
#     print(ret.group()) # 通过ret.group()获取真正的结果


# match 从头开始匹配,相当于search中的正则表达式加上一个^
# ret = re.match('\d+$','172sjkhk按实际花费928')
# print(ret)

# 字符串处理的扩展 : 替换 切割
# split
# s = 'alex|taibai|egon|'
# print(s.split('|'))
# s = 'alex83taibai40egon25'
# ret = re.split('\d+',s)
# print(ret)

# sub # 谁 旧的 新的 替换次数
# ret = re.sub('\d+','H','alex83taibai40egon25')
# print(ret)
#
# ret = re.sub('\d+','H','alex83taibai40egon25',1)
# print(ret)

# subn 返回一个元组,第二个元素是替换的次数
# ret = re.subn('\d+','H','alex83taibai40egon25')
# print(ret)

# re模块的进阶 : 时间/空间
# compile 节省你使用正则表达式解决问题的时间
# 编译 正则表达式 编译成 字节码
# 在多次使用的过程中 不会多次编译
# ret = re.compile('\d+')   # 已经完成编译了
# print(ret)
# res = ret.findall('alex83taibai40egon25')
# print(res)
# res = ret.search('sjkhk172按实际花费928')
# print(res.group())

# finditer 节省你使用正则表达式解决问题的空间/内存
# ret = re.finditer('\d+','alex83taibai40egon25')
# for i in ret:
#     print(i.group())


# findall 返回列表 找所有的匹配项
# search  匹配就 返回一个变量,通过group取匹配到的第一个值,不匹配就返回None,group会报错
# match   相当于search的正则表达式中加了一个'^'

# spilt   返回列表,按照正则规则切割,默认匹配到的内容会被切掉
# sub/subn 替换,按照正则规则去寻找要被替换掉的内容,subn返回元组,第二个值是替换的次数

# compile  编译一个正则表达式,用这个结果去search match findall finditer 能够节省时间
# finditer 返回一个迭代器,所有的结果都在这个迭代器中,需要通过循环+group的形式取值 能够节省内存




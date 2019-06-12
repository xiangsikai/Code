# by luffycity.com

class Foo:
    # 类变量(静态字段)
    country = "中国"

    def __init__(self, name):
        # 实例变量(字段)
        self.name = name

    def func(self):
        pass

# 知识点一:
"""
# 准则:
#   实例变量(字段)访问时,使用对象访问,即: obj1.name
#     类变量(静态字段)访问时,使用类方法,即: Foo.country  (实在不方便时,才使用对象)

obj1 = Foo('季红')
obj2 = Foo('王晓东')
print(obj1.name)
print(Foo.country) # obj1.country
"""

# 知识点一:易错点
"""
obj1 = Foo('季红')
obj2 = Foo('王晓东')

# 练习1
# obj1.name = 'alex'
# print(obj1.name) # alex
# print(obj2.name) # 王晓东

# 练习2
# obj1.country = '美国'
# print(obj1.country) # 美国
# print(obj2.country) # 中国

# 练习3
# Foo.country = '美国'
# print(obj1.country) # 美国
# print(obj2.country) # 美国
"""


# 知识点一: 什么时候用类变量?
# 当所有对象中有共同的字段时且要改都改要删都删时,可以将 实例变量(字段) 提取到 类变量(静态字段)

























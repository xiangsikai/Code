# by luffycity.com
"""
getattr # 根据字符串的形式，去对象中找成员。
hasattr # 根据字符串的形式，去判断对象中是否有成员。
setattr # 根据字符串的形式，去判断对象动态的设置一个成员（内存）
delattr # 根据字符串的形式，去判断对象动态的设置一个成员（内存）
"""

import xx

# getattr
v1 = getattr(xx,'x1')
v2 = getattr(xx,'f1')
v2('杨森')

# hasattr
v3 = hasattr(xx,'x1')
v4 = hasattr(xx,'f1')
v4 = hasattr(xx,'f1')
v5 = hasattr(xx,'xxxxxxx')
print(v3,v4,v5)

# setattr
setattr(xx,'x2',999)
v6 = getattr(xx,'x2')
print(v6)

setattr(xx,'f2',lambda x:x+1)
v7 = getattr(xx,'f2')
v8 = v7(1)
print(v8)

# delattr
delattr(xx,'x1')
v9 = getattr(xx,'x1')
print(v9)
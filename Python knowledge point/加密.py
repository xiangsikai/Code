# by luffycity.com

import hashlib

SALT = b'2erer3asdfwerxdf34sdfsdfs90'

def md5(pwd):
    # 实例化对象
    obj = hashlib.md5(SALT)
    # 写入要加密的字节
    obj.update(pwd.encode('utf-8'))
    # 获取密文
    return obj.hexdigest() # 21232f297a57a5a743894a0e4a801fc3 # 66fbdc0f98f68d69cd458b0cee975fe3 # c5395258d82599e5f1bec3be1e4dea4a


user = input("请输入用户名:")
pwd = input("请输入密码:")
if user == 'oldboy' and md5(pwd) == 'c5395258d82599e5f1bec3be1e4dea4a':
    print('登录成功')
else:
    print('登录失败')
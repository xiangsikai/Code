# by luffycity.com
# else分支
# try:
#     print('aaa')  # 给某某某发邮件
#     # name
#     # [][1]
#     # 1/0
# except NameError:   # 网络不稳定,邮箱地址错误
#     print('name error')
# except IndexError:
#     print('index error')
# except Exception as e:
#     print('Exception')
# else:  # 当try中的代码不发生异常的时候 走else分支  如果发送成功了 进行一些处理
#     print('else')

# finally分支
# try:
#     print('aaa')  # 给某某某发邮件
#     name
#     # [][1]
#     # 1/0
# except NameError:   # 网络不稳定,邮箱地址错误
#     print('name error')
# except IndexError:
#     print('index error')
# except Exception as e:
#     print('Exception')
# else:  # 当try中的代码不发生异常的时候 走else分支  如果发送成功了 进行一些处理
#     print('else')
# finally: # 无论如何都会被执行
#     print('finally')

# def func():
#     f = open('file')
#     try:
#         while True:
#             for line in f:
#                 if line.startswith('a'):
#                     return line
#     except:
#         print('异常处理')
#     finally:   # 即使return也会先执行fianlly中的代码
#         f.close()

# try:
#     f = open('www','w')
#     f.read()
# finally:   # 即使遇到报错,程序结束,也会先执行finally中的代码,然后再结束程序
#     f.close()
#     print('文件已经关闭了')

# finally用来回收一些操作系统的资源 : 数据库连接 打开的文件句柄 网络连接

# 异常处理的几种情况
# try ... except
# try ... except ... else
# try ... finally
# try ... except ... finally
# try ... except ... else ... finally

# 主动抛出异常 : 是给其他开发者用的
# raise ValueError
# raise ValueError('你写的不对')
# django是别人写的程序 框架 --> 程序员用

# 断言 - 语法
# assert 1==2  # 只能接受一个布尔值  False
# assert 1==1  # 只能接受一个布尔值  False
# print(123456)
# if 1 == int(input()):
#     pass
# else:
#     raise AssertionError


# 自定义异常 :面向对象之后

# 异常处理的忠告,在最外层的异常处理应该在所有的开发结束之后才放
# main()
    #sdhjlkghl

# try:
#     main()
# except Exception as e:
#     把e报错写到文件里

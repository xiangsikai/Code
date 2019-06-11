# by luffycity.com

# 死循环
# count = 1
# while count <= 5:
#     print("喷死你..")
#     count = count + 1
# 数数  1-100

# count = 1
# while count < 101:
#     print(count)
#     count = count + 2

# 让用户一直去输入内容, 并打印. 直到用户输入q的时候退出程序
# while True:
#     content = input("请输入一句话,(输入q退出程序):")
#     if content == 'q':
#         break   # 打断. 终止当前本层循环
#     print(content)

# flag = True
# while flag:
#     content = input("请输入一句话,(输入q退出程序):")
#     if content == 'q':
#         flag = False   # 打断. 终止当前本层循环
#     print(content)
# else:
#     print("123")


# while True:
#     content = input("请输入一句话,(输入q退出程序):")
#     if content == 'q':
#         continue   # 停止当前本次循环. 继续执行下一次循环
#     print(content)

# break和continue的区别: break是彻底的停止掉当前层循环. continue停止当前本次循环,继续执行下一次循环



# count = 1
# while count <= 10:
#     if count == 4:
#         count = count + 1
#         continue # 用来排除一些内容
#     print(count)
#     count = count + 1

# 必须要写
# count = 1
# while count <= 20:
#     if count == 10:
#         break # 不会触发else的执行,  while...else...是一个整体. break的时候彻底的停止这个整体
#     print(count)
#     count = count + 1
# else:   # 当上面的条件不成立的时候执行这个else中的代码
#     print("数完了")



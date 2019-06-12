# by luffycity.com

# 递归函数, 自己调用自己
# count = 1
# def func():
#     global count
#     print("alex是很帅的", count)
#
#     count = count + 1
#     func()
# func()
# 递归深度. 你可以自己掉用自己的次数,
# 官方文档中递归最大深度是1000. 在这之前就会给你报错

# 遍历 D:/sylar文件夹, 打印出所有的文件和普通文件的文件名
# import os
# def func(filepath, n): # d:/sylar/
#     # 1,打开这个文件夹
#     files = os.listdir(filepath)
#     # 2. 拿到每一个文件名
#     for file in files:  # 文件名
#         # 3. 获取到路径
#         f_d = os.path.join(filepath, file) # d:/sylar/文件名/
#         # 4. 判断是否是文件夹
#         if os.path.isdir(f_d):
#             # 5. 如果是文件夹. 继续再来一遍
#             print("\t"*n, file,":") # 打印文件名
#             func(f_d, n + 1)
#         else:   #  不是文件夹. 普通文件
#             print("\t"*n, file)
#
# func("d:/sylar",0)


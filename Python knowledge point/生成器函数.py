# by luffycity.com

# def func():
#     print("娃哈哈")
#     yield 1 # return和yield都可以返回数据
#     print("呵呵呵")
#
#
# gen = func() # 不会执行你的函数. 拿到的是生成器


# 函数中如果有yield 这个函数就是生成器函数. 生成器函数() 获取的是生成器. 这个时候不执行函数
# yield: 相当于return 可以返回数据. 但是yield不会彻底中断函数. 分段执行函数.
# gen.__next__() 执行函数. 执行到下一个yield.
# gen.__next__()  继续执行函数到下一个yield.


# def order():
#     lst = []
#     for i in range(10000):
#         lst.append("衣服"+str(i))
#     return lst
#
# ll = order()

# def order():
#     for i in range(10000):
#         yield "衣服"+str(i)
# g = order() # 获取生成器
# mingwei = g.__next__()
# print(mingwei)
# zhaoyining = g.__next__()
# print(zhaoyining)


# send() 和__next__()是一样的. 可以执行到下一个yield, 可以给上一个yield位置传值
# def func():
#     print("我是第一个段")
#     a = yield 123
#     print(a)
#     print("石可心是第二段")
#     b = yield 456
#     print(b) # ??
#     print("赵一宁是第三段")
#     c = yield 789
#     print(c)
#     print("刘伟是最后一个段")
#     yield 79  # 最后收尾一定是yield
#
#
#
# g = func()
# print(g.__next__()) # 没有上一个yield 所以不能使用send() 开头必须是__next__()
# print(g.send("煎饼果子"))
# print(g.send("韭菜盒子"))
# print(g.send("锅包肉"))  ## ??

# def eat():
#     print("我吃什么啊")
#     a =  yield  "馒头"
#     print("a=",a)
#     b =  yield  "鸡蛋灌饼"
#     print("b=",b)
#     c =  yield  "韭菜盒子"
#     print("c=",c)
#     yield  "GAME OVER"
# gen = eat()      # 获取生成器
#
# ret1 = gen. __next__()
# print(ret1) # 馒头
# ret2 = gen.send("胡辣汤")
# print(ret2)
#
# ret3 = gen.send("狗粮")
# print(ret3)
# ret4 = gen.send( "猫粮")
# print(ret4)

# def func():
#     yield 1
#     yield 13
#     yield 26
#     yield 88
#     yield 46
#     yield 100
#
#
# for i in func(): # for的内部一定有__next__()
#     print(i)
#
# print(list(func())) # 内部都有__next__()





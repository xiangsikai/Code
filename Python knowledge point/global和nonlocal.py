
# a = 10 # 全局变量本身就是不安全的, 不能随意修改, 闭包
# def func():
#     global a  # 1. 可以把全局中的内容引入到函数内部 , 2. 在全局创建一个变量
#     # a = 20
#     a += 10 # a = a+10
#     print(a)

#
# func()
# print(a)
# a = 10
# def outer():
#
#     def inner(): # 在inner中改变a的值
#         nonlocal a # 寻找外层函数中离他最近的那个变量
#         a = 20
#     inner()
#
# outer()


a = 1
def fun_1():
    a = 2
    def fun_2():
        global a
        a = 3
        def fun_3():
            a = 4
            print(a)
        print(a)
        fun_3()
        print(a)
    print(a)
    fun_2()
    print(a)
print(a)
fun_1()
print(a)










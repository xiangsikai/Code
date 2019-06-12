# by luffycity.com


class Account(object):
    func_list = ['login', 'logout', 'register']

    def login(self):
        """
        登录
        :return:
        """
        print('登录111')

    def logout(self):
        """
        注销
        :return:
        """
        print('注销111')

    def register(self):
        """
        注册
        :return:
        """
        print('注册111')

    def run(self):
        """
        主代码
        :return:
        """
        print("""
            请输入要执行的功能：
                1. 登录
                2. 注销
                3. 注册
        """)

        choice = int(input('请输入要执行的序号:'))
        func_name = Account.func_list[choice-1]

        # func = getattr(Account,func_name) # Account.login
        # func(self)

        func = getattr(self, func_name)  # self.login
        func()

obj1 = Account()
obj1.run()

obj2 = Account()
obj2.run()
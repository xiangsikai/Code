# by luffycity.com



class User:
    def __init__(self, user, pwd, email):
        self.user = user
        self.pwd = pwd
        self.email = email

user_list = []

# obj = User('alex1','123','xx@live.com')
obj = {'user':'alex1','pwd':123,'email':'asdf@live.com'} # dict({'user':'alex1','pwd':123,'email':'asdf@live.com'})
user_list.append(obj)

# obj = User('alex2','123','xx@live.com')
obj = {'user':'alex1','pwd':123,'email':'asdf@live.com'}
user_list.append(obj)

# obj = User('alex3','123','xx@live.com')
obj = {'user':'alex1','pwd':123,'email':'asdf@live.com'}
user_list.append(obj)


for row in user_list:
    # print(row.user,row.pwd,row.email)
    print(row['user'],row['pwd'],row['emailr'])








class Aniaml(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def eating(self):
        print("eating.....")

    def sleeping(self):
        print("sleeping.....")

class Fly(object):

    def flying(self):
        print("flying")

class Youyong(object):

    def youyong(self):
        print("游泳....")



class FlyYouyong(object):
    def youyong(self):
        print("游泳....")
    def flying(self):
        print("flying")


class Dog(Aniaml,FlyYouyong):pass

alex=Dog("alex",123)
print(alex.sleeping())
print(alex.flying())




# by luffycity.com
"""
创建三个学校且三个学校的设施内容等都是一致.
"""

class School(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def speech(self):
        print('讲课')

obj1 = School('老男孩北京校区', '美丽富饶的沙河')
obj2 = School('老男孩上海校区', '浦东新区')
obj3 = School('老男孩深圳校区', '南山区')
class Teacher(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary
        self.school = None

t1 = Teacher('李杰', 19, 188888)
t2 = Teacher('艳涛', 18, 60)
t3 = Teacher('女神',16, 900000)
# ############## 老师分配校区
t1.school = obj1
t2.school = obj1
t3.school = obj2
# ####################################
# 查看t1老师,所在的校区名称/地址
print(t1.school.name)
print(t1.school.address)
print(t1.name)
print(t1.age)
t1.school.speech()


































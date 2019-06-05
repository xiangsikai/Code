class Student(object):
    """学生类"""

    def __init__(self,name,gender,age):
        #学生名称
        self.name = name
        #学生性别
        self.gender = gender
        #学生年龄
        self.age = age
        #学生初始成绩
        self.score = 0

    #方法:修改学生成绩,教师可以进行修改
    def modify_score(self,new_score):
        self.score = new_score
class Teacher(object):
    """教师类"""

    def __init__(self,tech_name,tech_gender,tech_age,tech_sal):
        #教师姓名
        self.tech_name = tech_name
        #教师年龄
        self.tech_gender = tech_gender
        #教师性别
        self.tech_age = tech_age
        #教师工资
        self.tech_sal = tech_sal
        #绑定班级与课程,一对多
        self.tech_classroom = {}

    #将班级与课程进行绑定
    def add_tech_classroom(self,class_name,class_obj):
        self.tech_classroom[class_name] = class_obj

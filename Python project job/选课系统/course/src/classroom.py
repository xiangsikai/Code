class Classroom(object):
    """班级类"""

    def __init__(self,class_name,course_obj):
        #班级名称
        self.class_name = class_name
        #学习课程
        self.course_obj = course_obj
        #使用字典形式包含每个学生，一对多
        self.class_student = {}

from src.classroom import Classroom
from src.course import Course
from src.student import Student
from src.teacher import Teacher


class School(object):
    """学校类"""

    def __init__(self,name,address):
        #学校名称
        self.name = name
        #学校地址
        self.address = address
        #绑定课程
        self.sch_course = {}
        #绑定班级
        self.sch_classroom = {}
        #绑定教师
        self.sch_teacher = {}
        #绑定学生
        self.sch_student = {}

    #1.方法：创建课程#课程名，价格，周期
    def create_course(self,course_name,course_price,course_time):
        #1.创建课程对象，赋值变量
        course_obj = Course(course_name,course_price,course_time)
        #2.根据课程名称为key，课程对象为value,存放Course的内存地址
        self.sch_course[course_name] = course_obj

    #2.方法：查看课程信息
    def show_course(self):
        #1.for循环查找
        for course in self.sch_course:
            #2.变量 = 字典[key]
            course_obj = self.sch_course[course]
            #3.打印课程信息
            print('课程名称[%s]\t课程价格[%s]\t学习周期[%s]'%(course_obj.course_name,
                                                            course_obj.course_price,
                                                            course_obj.course_time))

    #3.方法：修改课程
    def modify_course(self,course_name,course_price,course_time):
        #1.修改赋值变量
        course_obj = Course(course_name,course_price,course_time)
        #2.修改到字典中
        self.sch_course[course_name] = course_obj

    #4.方法：创建班级
    def create_classroom(self,class_name,course_obj):
        #1.创建班级对象，赋值变量
        class_obj = Classroom(class_name,course_obj)
        #2.根据班级名称为key，班级对象为value来建立对应关系,添加到字典
        self.sch_classroom[class_name] = class_obj

    #5.方法：查看班级
    def show_classroom(self):
        #1.循环打印班级信息
        for classroom in self.sch_classroom:
            class_obj = self.sch_classroom[classroom]
            print("班级名称[%s]\n学习课程[%s]"%(class_obj.class_name,class_obj.course_obj.course_name))
            if self.sch_student:
                student = class_obj.class_student[classroom].name
                print("班级成员[%s]"%student)

    #6.方法：修改班级
    def modify_classroom(self,class_name,course_obj):
        #1.添加班级对象
        class_obj = Classroom(class_name,course_obj)
        #2.修改字典中班级信息
        self.sch_classroom[class_name] = class_obj

    #7.方法：创建教师
    def create_teacher(self,tech_name,tech_gender,tech_age,tech_sal,class_name,class_obj):
        #1.创建教师对象，赋值变量
        teacher_obj = Teacher(tech_name,tech_gender,tech_age,tech_sal)
        #2.添加班级与课程的对象信息在教师类下
        teacher_obj.add_tech_classroom(class_name,class_obj)
        #3.根据教师名称为key，教师对象为value来建立对应关系
        self.sch_teacher[tech_name] = teacher_obj

    #8.方法：查看教师
    def show_teacher(self):
        if self.sch_teacher:
            #1.循环打印教师信息
            for teacher in self.sch_teacher:
                tech_obj = self.sch_teacher[teacher]
                print("教师姓名[%s] 教师年龄[%s] 教师性别[%s] 教师工资[%s]"%(tech_obj.tech_name,tech_obj.tech_gender,tech_obj.tech_age,tech_obj.tech_sal))
        else:
            print("无教师")

    #9.方法：修改教师
    def modify_teacher(self,tech_name,tech_gender,tech_age,tech_sal,class_name,class_obj):
        #1.创建教师对象
        teacher_obj = Teacher(tech_name,tech_gender,tech_age,tech_sal)
        #2.修改课程绑定
        teacher_obj.add_tech_classroom(class_name,class_obj)
        #3.修改教师存储
        self.sch_teacher[tech_name] = teacher_obj

    #10.方法：创建学生 #学生名称，性别，年龄，班级名称
    def create_student(self,name,gender,age,class_name):
        #1.创建学生对象，赋值变量
        student_obj = Student(name,gender,age)
        #2.根据学生名称为key，学生对象为value来建立对应关系
        self.sch_student[name] = student_obj
        #3.建立学生和班级的关联关系
        class_obj = self.sch_classroom[class_name]
        #4.存放学生对象，班级类的class_student存放学生对象
        class_obj.class_student[class_name] = student_obj
        #5.更新班级信息
        self.sch_classroom[class_name] = class_obj

    #11.方法：老师查看学生的关联信息。
    def show_teacher_stu_info(self,tech_name):
        #1.取出教师对象
        teacher_obj = self.sch_teacher[tech_name]
        #2.循环教师对象下面的班级
        for t in teacher_obj.tech_classroom:
            #3.取出班级字典内的多个班级
            class_obj = self.sch_classroom[t]
            #4.创建空列表
            stu_list = []
            #5.循环班级对象下面的学生
            for j in class_obj.class_student:
                #6.班级学生打印到空列表
                stu_list.append(j)
                #7.输出班级，课程，学生，信息
            print('班级名称[%s]\t课程[%s]\t学生[%s]'%(class_obj.class_name,
                                                    class_obj.course_obj.course_name,
                                                    stu_list))

    #12.方法：教师更该学生成绩，教师姓名，学生姓名，新成绩
    def modify_student_score(self,tech_name,stu_name,new_score):
        #1.创建存放学生名的列表
        stu_list = []
        #2.生成教师对象
        tech_obj = self.sch_teacher[tech_name]
        #3.循环打印教师下的班级
        for i in tech_obj.tech_classroom:
            #4.生成班级对象
            class_obj = tech_obj.tech_classroom[i]
            #5.生成学生对象
            stu_obj = class_obj.class_student[i]
            #6.生成学生名
            stuname = stu_obj.name
            #7.添加学生名到列表
            stu_list.append(stuname)
            #8.判断是否是需要修改的学生
            if  stu_name in stu_list:
                #9.修改学生成绩
                stu_obj.modify_score(new_score)
                #10.更新教师对象
                self.sch_teacher[tech_name] = tech_obj

    #13.方法：查看学生
    def show_student(self,):
        if self.sch_student:
            for stu in self.sch_student:
                student_obj = self.sch_student[stu]
                student_name = student_obj.name
                student_age = student_obj.age
                student_gender = student_obj.gender
                student_score = student_obj.score
                print("姓名[%s]   性别[%s]    年龄[%s]    成绩[%s]"%(student_name,student_gender,student_age,student_score))
        else:
            print("无学生")
import shelve
import os,sys
core_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(core_path)

from conf import settings
from src.school import School
from src.teacher import Teacher
from src.course import Course
#from src.classroom import Student
from src.student import Student

class Center(object):
    """主菜单类"""
    #方法：用户菜单
    def run(self):
        #退出的标记
        exit_flag = False
        menu = u'''
            \033[34;1m
            1.教师视图
            2.学校视图
            3.退出\033[0m
        '''
        #循环输出
        while not exit_flag:
            #打印菜单
            print(menu)
            #用户交互
            user_option = input('请输入要管理的视图>>:')
            #判断用户输入，执行或退出
            if user_option == '1':
                Teacher_view()
            elif user_option == '2':
                School_view()
            elif user_option == '3':
                exit_flag = True
            else:
                print('输入的选项不正确，请重新输入')

class School_view(object):
    """学校视图执行类"""
    def __init__(self):
        #判断该路径下是否存在.dat结尾的文件路径
        if os.path.exists(settings.school_file + '.dat'):
            #同过shelve打开这个文件
            self.school_file = shelve.open(settings.school_file)
            #管理这个文件
            self.school_manager()
            #关闭这个文件
            self.school_file.close()
        else:
             print('没有学校和班级的数据，请先创建')
             #创建文件
             self.init_school()
             #管理文件
             self.school_manager()
             #关闭文件
             self.school_file.close()

    #1.方法：创建文件
    def init_school(self):
        #1.创建新文件
        self.school_file = shelve.open(settings.school_file)
        #2.创建两所学校
        self.school_file['北京'] = School('北京总校','北京')
        self.school_file['上海'] = School('上海分校','上海')

    #2.方法:学校管理
    def school_manager(self):
        #1.打印学校名字
        while True:
            #2.循环打印出文件中的学校名称
            for sch_name in self.school_file:
                print('学校名称[%s]'%sch_name)
            #3.用户输出需要管理的学校名称
            sch_option =input('请输入要管理的学校名称').strip()
            #4.判断如果学校存在就把学校取出
            if sch_option in self.school_file:
                #5.赋值sch_option为全局变量
                self.sch_option = sch_option
                #6.赋值school_obj为School类的内存地址
                self.school_obj = self.school_file[sch_option]
                #7.循环打印输出管理菜单
                while True:
                    menu='''
                        欢迎来到[%s]校区
                        添加课程 add_course
                        添加班级 add_classroom
                        添加讲师 add_teacher
                        添加学生 add_student
                        修改课程 mod_course
                        修改班级 mod_classroom
                        修改教师 mod_teacher
                        查看班级 show_classroom
                        查看课程 show_course
                        查看讲师 show_teacher
                        查看学生 show_student
                        退出     q
                    '''%sch_option
                    print(menu)
                    user_choice = input("请选择以上操作>>:").strip()
                    #8.执行字符串命令，如果存在user_choice方法就成立，反射操作
                    if hasattr(self,user_choice):
                        #9.通过反射，执行user_choice用户执行的方法。
                        getattr(self,user_choice)()
                    if user_choice == "q":
                        self.school_file.close()
                        exit()

    #3.方法：添加课程
    def add_course(self):
        #1.用户输入添加课程信息
        course_name = input("请输入课程名称").strip()
        course_price = input("请输入课程价格").strip()
        course_time = input("请输入课程周期").strip()
        #2.判断如果输入课程名存在就成立
        if course_name in self.school_obj.sch_course:
            print("该课程名已存在")
        else:
            #3.不成立就调用crete_course方法，创建课程
            self.school_obj.create_course(course_name,course_price,course_time)
            print("[%s]课程添加成功"%course_name)
        #4.创建成功后更新文件。前面是key（必须是字符串） 后面是value（可以是变量）。
        self.school_file.update({self.sch_option:self.school_obj})

    #4.方法：添加班级
    def add_classroom(self):
        #1.用户输入班级信息
        class_name = input("请输入班级名称").strip()
        class_course = input("请输入课程").strip()
        #2.判断班级是否不存在字典中
        if class_name not in self.school_obj.sch_classroom:
            #3.判断课程是否已存在
            if class_course in self.school_obj.sch_course:
                #4.赋值课程内的内存地址
                course_obj = self.school_obj.sch_course[class_course]
                #5.通过create_class创建班级，并将课程信息类以value行式添加到字典
                self.school_obj.create_classroom(class_name,course_obj)
                #6.创建成功后更新文件信息
                self.school_file.update({self.sch_option:self.school_obj})
                print("班级创建成功")
            else:
                print("课程不存在")
        else:
            print("班级不存在")

    #5.方法：添加教师
    def add_teacher(self):
        #1.用户输入信息
        tech_name = input("教师姓名>>:")
        tech_age  = input("教师年龄>>:")
        tech_gender = input("教师性别>>:")
        tech_sal = input("教师工资>>:")
        tech_class = input("教师授课班级>>:")
        #2.判断教师班级是否存在
        if tech_class in self.school_obj.sch_classroom:
            #3.赋值班级key下的value信息
            class_obj = self.school_obj.sch_classroom[tech_class]
            #4.判断教师是否不存在
            if tech_name not in self.school_obj.sch_teacher:
                #5.创建教师，
                self.school_obj.create_teacher(tech_name,
                                               tech_age,
                                               tech_gender,
                                               tech_sal,tech_class,class_obj)
                print('教师招聘成功')
                self.school_file.update({self.sch_option:self.school_obj})
            else:
                #6.调用modify_teacer修改教师信息
                self.school_obj.modify_teacher(tech_name,tech_age,tech_gender,tech_sal,tech_class,class_obj)
                print('修改教师信息成功')
            #7.创建成功更新文件
            self.school_file.update({self.sch_option:self.school_obj})
        else:
            print('请先创建班级')

    #6.方法：添加学生
    def add_student(self):
        student_name = input("学生姓名>>：").strip()
        student_age = input("学生年龄>>:").strip()
        student_gender = input("学生性别>>:").strip()
        if student_name not in self.school_obj.sch_student:
            student_classroom = input("输入绑定班级>>:").strip()
            if student_classroom in self.school_obj.sch_classroom:
                self.school_obj.create_student(student_name,student_gender,student_age,student_classroom)
                self.school_file.update({self.sch_option:self.school_obj})
                print("添加学生完成！")
            else:
                print("无所在班级！")
        else:
            print("该学生已经存在！")

    #7.方法：修改课程
    def mod_course(self):
        #1.创建修改课程信息
        course_name = input("请输入修改课程名称").strip()
        course_price = input("请输入修改课程价格").strip()
        course_time = input("请输入修改课程周期").strip()
        #2.判断课程名是否存在
        if course_name in self.school_obj.sch_course:
            self.school_obj.modify_course(course_name,course_price,course_time)
            print("[%s]课程修改成功"%course_name)
        else:
            print("该课程不存在，请先创建")
        #3.创建成功后更新存储文件
        self.school_file.update({self.sch_option:self.school_obj})

    #8.方法：修改班级
    def mod_classroom(self):
        #1.用户输入班级信息
        class_name = input("请输入班级名称").strip()
        class_course = input("请输入课程").strip()
        #2.判断班级是否不存在字典中
        if class_name not in self.school_obj.sch_classroom:
            #3.判断课程是否已存在
            if class_course in self.school_obj.sch_course:
                #4.修改班级信息
                self.school_obj.modify_classroom(class_name,class_course)
                print("修改班级成功")
                #5.更新文件信息
                self.school_file.update({self.sch_option:self.school_obj})
            else:
                print("课程不存在请创建课程")
        else:
            print("班级不存在请创建班级")

    #9.方法：修改教师
    def mod_teacher(self):
        #1.用户输入信息
        tech_name = input("修改教师姓名>>:")
        tech_age  = input("修改教师年龄>>:")
        tech_gender = input("修改教师性别>>:")
        tech_sal = input("修改教师工资>>:")
        tech_class = input("修改教师授课班级>>:")
        #2.判断教师班级是否存在
        if tech_class in self.school_obj.sch_classroom:
            #3.赋值班级key下的value信息
            class_obj = self.school_obj.sch_classroom[tech_class]
            #4.判断教师是否存在
            if tech_name in self.school_obj.sch_teacher:
                self.school_obj.modify_teacher(tech_name,tech_age,tech_gender,tech_sal,tech_class,class_obj)
                print("教师信息修改成功")
                #5.更新文件
                self.school_file.update({self.sch_option:self.school_obj})
            else:
                print("教师不存在请创建教师")
        else:
            print("班级不存在请创建班级")

    #10.方法：查看班级
    def show_classroom(self):
        self.school_obj.show_classroom()

    #11.方法：查看课程
    def show_course(self):
        self.school_obj.show_course()

    #12.方法：查看教师
    def show_teacher(self):
        self.school_obj.show_teacher()

    #13.方法：查看学生
    def show_student(self):
        self.school_obj.show_student()

class Teacher_view(object):
    """老师视图执行类"""

    def __init__(self):
        #判断该路径下是否存在.dat结尾的文件路径
        if os.path.exists(settings.school_file + '.dat'):
            self.school_file = shelve.open(settings.school_file)
            self.teacher_manager()
            self.school_file.close()
        else:
            print('讲师不在，请先创建学校')
            exit()

    #1.方法:教师管理
    def teacher_manager(self):
        #1.打印学校名字
        while True:
            #2.循环打印出文件中的学校名称
            for sch_name in self.school_file:
                print('学校名称[%s]'%sch_name)
            #3.用户输出需要管理的学校名称
            sch_option =input('   <北京--上海>  '
                              '您是哪个学校的老师').strip()
            #4.判断如果学校存在就把学校取出
            if sch_option in self.school_file:
                #5.赋值sch_option为全局变量
                self.sch_option = sch_option
                #6.赋值school_obj为School类的内存地址
                self.school_obj = self.school_file[sch_option]
            while True:
                teacher_login = input("请输入您的姓名>>:").strip()
                if teacher_login in self.school_obj.sch_teacher:
                    while True:
                        menu='''
                        <欢迎[%s]老师   来到[%s]学院>
                            查看班级 show_classroom
                            查看课程 show_course
                            查看讲师 show_teacher
                            查看学生 show_student
                            修改成绩 mod_stu_score
                            退出     q
                        '''%(teacher_login,sch_option)
                        print(menu)
                        user_choice = input("请选择以上操作>>:").strip()
                        #8.执行字符串命令，如果存在user_choice方法就成立，反射操作
                        if hasattr(self,user_choice):
                            #9.通过反射，执行user_choice用户执行的方法。
                            getattr(self,user_choice)()
                        if user_choice == "q":
                            self.school_file.close()
                            exit()
                else:
                    print("教师不存在")

      #11.方法：查看班级

    #2.方法:查看班级
    def show_classroom(self):
        self.school_obj.show_classroom()

    #3.方法：查看课程
    def show_course(self):
        self.school_obj.show_course()

    #4.方法：查看教师
    def show_teacher(self):
        self.school_obj.show_teacher()

    #5.方法：查看学生
    def show_student(self):
        self.school_obj.show_student()

    #6.方法：修改成绩
    def mod_stu_score(self):
        tea_name = input("输入修改成绩的老师>>:").strip()
        if tea_name in self.school_obj.sch_teacher:
            stu_name = input("输入被修改成绩的学生>>:").strip()
            if stu_name in self.school_obj.sch_student:
                mod_score = input("输入需要修改的成绩>>：").strip()
                self.school_obj.modify_student_score(tea_name,stu_name,mod_score)
                self.school_file.update({self.sch_option:self.school_obj})
                print("修改成功！")
            else:
                print("没有该学生！")
        else:
            print("没有该老师")






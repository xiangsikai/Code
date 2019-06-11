from django.shortcuts import render,HttpResponse,redirect
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        # 数据库执行 select * from user where username='x' and password='x'
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # 判断
        # .firest() 直接变为对象，没有则输出None。
        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        # .count() 获取个数，没有则输出0。
        # count = models.UserInfo.objects.filter(username=u,password=p).count()
        if obj:
            return redirect('/cmdb/index/')
        else:
            return render(request,'login.html')
    else:
        # PUT,DELETE,HEAD,OPTION ...
        return redirect('/index/')

def index(request):
    return render(request,'index.html')

def user_info(request):
    user_list = models.UserInfo.objects.all()
    return render(request,'user_info.html',{"user_list":user_list})

def user_detail(request,nid):
    # 只获取一条数据
    obj = models.UserInfo.objects.filter(id=nid).first()
    print(obj)
    # 取单条数据如果不存在直接报错
    # models.UserInfo.objects.get(id=nid)
    return render(request, 'user_detail.html', {'obj':obj})

from app01 import models
def orm(request):
    # 增
    # 创建、增加数据 create()
    # models.UserInfo.objects.create(username='root',password='123')

    # 创建、增加数据
    # dic = {'username':'eric','password':'666'}
    # models.UserInfo.objects.create(**dic)

    # 创建、增加数据
    # obj = models.UserInfo(username='xsk',password='123')
    # obj.save()

    # 查
    # 获取表内所有数据  all()
    # result返回的是QuerySet类型 => Django类 => []
    # 全部都是UserInfo的对象[obj(id,username,password),obj,obj]
    # result = models.UserInfo.objects.all()
    # for row in result:
    #     print(row.id,row.username,row.password)
    # print(result)

    # 获取username字段中带有root的一列对象值 filter()
    result = models.UserInfo.objects.filter(username='root')
    # 获取username字段中带有root与password字段中带有123的一行对象值 filter()
    # result = models.UserInfo.objects.filter(username='root',password="123")
    # for row in result:
    #     print(row.id,row.username,row.password)

    # 删
    # 删除指定字段的行
    # models.UserInfo.objects.filter(id=4).delete()
    # 删除指定多个字段的行
    # models.UserInfo.objects.filter(username='root',password="123").delete()

    # 改
    # 修改所有名为password字段内的所有值变为888
    # models.UserInfo.objects.all().update(password="888")

    # 修改指定id的行修改字段内的值
    # models.UserInfo.objects.filter(id="3").update(password="777")

    return HttpResponse('orm')

from django.views import View
class Home(View):

        def dispatch(self, request, *args, **kwargs):

            # 调用父类中的dispatch，保留父类功能的基础上增加功能
            print("定制功能1")
            result = super(Home,self).dispatch(request,*args,**kwargs)
            print("定制功能2")
            return result

        def get(self,request):
            print(request.method)
            return render(request,'home.html')

        def post(self,request):
            print(request.method)
            return render(request, 'home.html')
















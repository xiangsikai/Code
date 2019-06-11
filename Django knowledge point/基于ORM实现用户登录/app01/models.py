from django.db import models

# Create your models here.

# 类
# 默认生成表名：app01_userinfo
class UserInfo(models.Model):
    # id列，自增，主键
    # 用户名列：字符串类型，指定长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

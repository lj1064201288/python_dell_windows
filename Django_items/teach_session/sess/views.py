from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
# Create your views here.



def Mysess(request):
    print(request.session)
    print(type(request.session))
    # 如果session里面没有teacher_name值，则返回NoName
    print(request.session.get("teacher_name", "Noname"))
    # 清除session的值
    request.session.clear()
    print('In Sess')


def student(request):
    stus = Student.objects.all()
    # 两个参数:
    # 1.数据来源
    # 2.单页显示的数量
    p = Paginator(stus, 40)
    # 对Paginator进行设置或者对变量属性使用
    print(p)
    print(p.count) # p里面有多少数据
    print(p.page_range)# 页码列表，从1开始
    print(p.num_pages) # 多少页数
    # 取得第三页的内容
    # 如果没有，报异常InvalidPage
    p.page(3)

    return p

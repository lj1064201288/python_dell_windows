from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse
from django.views import defaults
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
# Create your views here.


def teacher(request):
    return HttpResponse('这是teacher的一个视图')

def v2_exception(request):
    raise Http404
    return HttpResponse('OK')

def v10_1(request):
    return  HttpResponseRedirect('/v11')

def v10_2(request):
    return HttpResponseRedirect(reverse('v11'))

def v11(request):
    return HttpResponse('这是v11的返回呀！')

def v8_get(request):
    rst = ''
    for k, v in request.GET.items():
        rst += k + " ==> " + v
        rst += ', '
    return HttpResponse('Get value of Request is {0}'.format(rst))

def v9_get(request):
    # 渲染模块并且返回
    return render_to_response('for_post.html')

def v9_post(request):
    rst = ''
    for k,v in request.POST.items():
        rst += k + "==>" + v
        rst += ','
    return HttpResponse('Get value of POST is {}'.format(rst))

def render_test(request):
    # 环境变量
    c = dict()
    rsp = render(request, 'render.html')
    return  rsp

def render2_test(request):
    # 环境变量
    c = {
        'name':'liujun',
        'name1':'yangzhibo',
        'name2':'hehaichuan',
        'name3':'tangkai',
    }
    rsp = render(request, 'render2.html', context=c)
    return  rsp

def render3_test(request):
    t = loader.get_template('render2.html')
    rsp = t.render({'name':'刘俊'})

    return HttpResponse(rsp)

def render4_test(request):
    c = {
        'name': 'liujun',
        'name1': 'yangzhibo',
        'name2': 'hehaichuan',
        'name3': 'tangkai',
    }
    rsp = render_to_response( 'render2.html', context=c)
    return rsp

def get_404(request):
    return defaults.page_not_found(request, template_name='render.html')

def welcome(request):
    return  HttpResponse('欢迎来到我的主页!')
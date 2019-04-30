from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def one(request):
    return render(request, r'one.html')


def two(request):
    # 传入的参数
    ct = {
        'name':'曹玲玲',
    }
    html = render(request, r'two.html', context=ct)
    return HttpResponse(html)


def three(request):
    source = [89,57,95,79,97,65,85]

    dt = {
        'source':source
    }

    html = render(request, r'three.html', context=dt)

    return HttpResponse(html)

def four(request):
    name = '阳志波'
    dt = {
        'name': name,
    }

    html = render(request, r'four.html', context=dt)

    return HttpResponse(html)


def five_get(request):
    return render(request, 'five_get.html')

def five_post(request):
    print(request.POST)
    return render(request, 'one.html')


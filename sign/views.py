from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, "sign/index.html")


'''
# 普通登陆
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            # return HttpResponse('login success!')
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request, 'sign/index.html', {'error': 'username or password error!'})


def event_manage(request):
    return render(request, "sign/event_manage.html")
'''

"""
# cookie登陆
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            response.set_cookie('user', username, 3600)  # 添加浏览器cookie
            return response
        else:
            return render(request, 'sign/index.html', {'error': 'username or password error!'})


def event_manage(request):
    username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    return render(request, "sign/event_manage.html", {"user": username})
"""

'''
# session登陆
# no such table: django_session 使用session需要有数据库
# python manage.py makemigrations
# python manage.py migrate
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)  # 添加浏览器cookie
            request.session['user'] = username  # 将session信息记录到浏览器
            return response
        else:
            return render(request, 'sign/index.html', {'error': 'username or password error!'})


def event_manage(request):
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, "sign/event_manage.html", {"user": username})
'''


# Django认证登陆
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # response.set_cookie('user', username, 3600)  # 添加浏览器cookie
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'sign/index.html', {'error': 'username or password error!'})


@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, "sign/event_manage.html", {"user": username})

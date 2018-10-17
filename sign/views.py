from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event
from sign.models import Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    event_list = Event.objects.all()
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, "sign/event_manage.html", {"user": username, "events": event_list})


@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name1 = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_name1)
    return render(request, "sign/event_manage.html", {"user": username, "events": event_list})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')  # 读取浏览器session
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一面
        contacts = paginator.page(paginator.num_pages)
    return render(request, "sign/guest_manage.html", {"user": username, "guests": contacts})


@login_required
def search_name_guest(request):
    username = request.session.get('user', '')
    search_name2 = request.GET.get("phone", "")
    guest_list = Guest.objects.filter(phone__contains=search_name2)
    return render(request, "sign/guest_manage.html", {"user": username, "guests": guest_list})


# 签到页面
@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    return render(request, "sign/sign_index.html", {"event": event})

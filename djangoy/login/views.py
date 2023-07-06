from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
# login/views.py
from django.shortcuts import render, redirect

from login.models import SiteUser

from login.forms import LoginForm

from login.forms import RegisterForm

from login.utils import hash_code

from djangoy import settings
from login import models
import datetime
from django.utils import timezone

from login.models import ConfirmString


# Create your views here

def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')

def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = SiteUser.objects.filter(name=username, password=hash_code(password)).first()
            if not user.has_confirmed:
                message = '该用户还未经过邮件确认！'
                return render(request, 'login/login.html', locals())
            if user:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['username'] = user.name
                return redirect('/index/')
            else:
                message = "用户名或者密码错误"
                return render(request, 'login/login.html', locals())
        else:
            message = "填写的登录信息不合法"
            return render(request, 'login/login.html', locals())

    login_form = LoginForm()
    return render(request, 'login/login.html', locals())

def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"

        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')

            same_name_user = SiteUser.objects.filter(name=username)
            if same_name_user:
                message = '用户名已经存在'
                return render(request, 'login/register.html', locals())

            same_email_user = SiteUser.objects.filter(email=email)
            if same_email_user:
                message = '该邮箱已经被注册了！'
                return render(request, 'login/register.html', locals())

            new_user = SiteUser(name=username, password=hash_code(password1), email=email)
            new_user.save()
            code = make_confirm_string(new_user)
            send_email(email, code)
            message = '请前往邮箱进行确认！'
            return redirect('/login/')

    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())

def logout(request):
    if request.session.get('is_login'):
        request.session.flush()
    return redirect('/login/')

def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())

    create_time = confirm.create_time
    now = timezone.now()
    if now > create_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
    return render(request, 'login/confirm.html', locals())


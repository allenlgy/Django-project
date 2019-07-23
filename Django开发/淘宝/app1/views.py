from django.shortcuts import render,redirect
from app1 import models
from .forms import UserForm,RegisterForm
import hashlib
# Create your views here.

def hash_code(s,salt='mysite'):
    h = hashlib.sha3_256()
    s+= salt
    h.update(s.encode())  #update 方法只接收bytes类型
    return h.hexdigest()

def index(request):

    pass
    return render(request,'login/index.html')

def register(request):
    if request.session.get('is_login',None):
        #  登录状态不允许注册
        return redirect('/index/')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = '请检查填写的内容!'

        if register_form.is_valid():  #　获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']

            if password1 != password2:
                message='两次输入的密码不同！'
                return render(request,'login/register.html',locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在，请重新选择用户名!'
                    return render(request,'login/register.html',locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱地址已经被注册，请使用别的邮箱!'

                    return render(request,'login/register.html')

                #　　当一切ｏｋ，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)  #加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 跳转到登录页面

    register_form = RegisterForm()
    return render(request,'login/register.html',locals())


def logout(request):
    if not request.session.get('is_login',None):

        return redirect('/index/')
    request.session.flush()  #删除当前回话数据和回话cookie，在用户退出后珊瑚虫

    return redirect('/index/')

def login(request):
    if request.session.get('is_login',None):  # 如果cookie的信息是这个，不允许重复登录
        return redirect('/index')

    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username=login_form.cleaned_data['username']#  确保密码用户名不为空
            password=login_form.cleaned_data['password']

            try:
                user = models.User.objects.get(name= username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')

                else:
                    message = '密码不正确!'

            except:
                message = '用户名不存在!'

        return render(request,'login/login.html',locals())

    login_form = UserForm()
    return render(request,'login/login.html')
# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from utils.email_send import send_register_email


class CustomBackend(ModelBackend):
    # 进行相应验证
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username)|Q(email=username))
            # 进行密码明文加密
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    # 利用面向对象解决登录验证
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # form验证成功
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            # 向数据库发起账号密码是否一致,进行认证
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    # 完成登录
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户未激活'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class ActiveUserView(View):
    # 完成邮箱验证
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html',{'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            # 判断邮箱是否存在
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form, 'msg': u'用户已经存在'})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_name, "register")
            return render(request, 'login.html')
        else:
            return render(request, 'register.html',{'register_form': register_form})


class ForgetPwdView(View):
    # 找回密码解决方案
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, 'forget')
            return render(request, 'send_success.html', {})
        else:
            return render(request, "forgetpwd.html", {'forget_form': forget_form})


class ResetView(View):
    # 完成邮箱验证
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {'email': email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email')
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {'email': email, 'msg': u'密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd1)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'email': email, 'modify_form': modify_form})


















# def user_login(request):
#     # 一般不使用该种方法登录验证
#     if request.method == 'POST':
#         user_name = request.POST.get('username','')
#         pass_word = request.POST.get('password', '')
#         # 向数据库发起账号密码是否一致
#         user = authenticate(username = user_name, password = pass_word)
#         if user is not None:
#             # 完成登录
#             login(request, user)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html', {'msg': '用户名或密码错误'})
#
#     elif request.method == 'GET':
#         return render(request, 'login.html', {})
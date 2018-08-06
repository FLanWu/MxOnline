# _*_ coding: utf-8 _*_
__author__ = 'hcfly'
__date__ = '18-8-2 下午4:19'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # 进行Form检测
    # username和password 为Char类型,并且为必填字段
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

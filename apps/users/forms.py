# coding=utf-8
# !/usr/bin/ env python
from captcha.fields import CaptchaField
from django import forms

__author__ = 'AllenQ'
__date__ = "22:17"


class RegisterForm(forms.Form):
    """注册表单校验"""
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    # error_messages定义 中文信息报错,返回给前端页面
    captcha = CaptchaField(required=True, error_messages={"invalid": "验证码错误"})
    pass


class ForgetPwdForm(forms.Form):
    """忘记密码表单校验"""
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})
    pass


class LoginForm(forms.Form):
    """登录表单校验"""
    # 必填 最大长度 最小长度
    # 注意 这里定义的username 和 password两个名称 必须要和穿过来的key值想通过
    # 否则不会做验证
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    pass

class ModifyPwdForm(forms.Form):
    """修改密码提交密码的表单校验"""
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

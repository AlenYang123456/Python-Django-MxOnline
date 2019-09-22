# coding=utf-8
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

import xadmin
# 基于函数的视图函数
from MxOnline.settings import MEDIA_ROOT
from users.views import IndexView, LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView
from organization.views import OrgView
# 处理静态文件url路径的方法
from django.views.static import serve

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    # 登录相关的url
    # url(r'^login/$',user_login,name="login"), 基于方法的视图---不推荐
    url(r'^login/$', LoginView.as_view(), name="login"),  # 基于类的视图---更加推荐 传递的是方法
    # url(r'^admin1/$', views.hello),
    # 配置注册页面--注册这里为什么没有r()
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    # 激活账号连接 配置url传参,获取url中的参数--注意是调用类里面的方法 必须加括号,否则报错
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    # 找回密码链接
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    # 忘记密码url
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    # 修改密码
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    # 课程机构首页
    url(r'^org-list/$', OrgView.as_view(), name="org-list"),
    # 配置上传文件的处理函数
    url(r'^media/(?P<path>.*)$',serve, {"document_root":MEDIA_ROOT}),

    # 课程机构url配置--按照url的分类做url的分发
    # namespace 是命名空间的概念,防止重复名称的作用
    url(r'^org/',include('organization.urls',namespace="org")),

    url(r'^users/', include('users.urls', namespace="users")),


]

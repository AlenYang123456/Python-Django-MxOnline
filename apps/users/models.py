# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
# 继承django自带的user,继承原有的字段,同时还能添加自己的字段
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    """定义用户模型"""
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('male', u'男'), ('female', u'女')), default='female')
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 依赖于Pillow这个库
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)

    class Meta:
        # 这里就是app的名称
        verbose_name = u"用户信息"
        # verbose_name_plural 如果不指定verbose_name_plural = verbose_name
        # 那么就会将"用户信息"后面加上s
        verbose_name_plural = verbose_name
        # db_table="表名"

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """邮箱验证码"""
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    # 如果不指定null=True 默认是不能为null
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型", choices=(("register", u"注册"), ("forget", u"忘记密码")),
                                 max_length=30)
    # 注意;这里datetime.now()去掉括号,防止以保存的时间作为时间
    # 注意 如果这里不加verbose_name="xxx" 那么在页面上就会展示英文名字 send_time
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name
    # def __unicode__(self):
    #     return "邮箱验证码-py2.x生效,3.x不生效"

    def __str__(self):
        return '{0}-({1})'.format(self.code,self.email)

    pass


class Banner(models.Model):
    """轮播图"""
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(max_length=100, upload_to="banner/%Y/%m", verbose_name=u"轮播图")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

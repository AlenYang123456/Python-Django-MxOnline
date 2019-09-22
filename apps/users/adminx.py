# coding=utf-8
# !/usr/bin/ env python

__author__ = 'AllenQ'
__date__ = '2019/10/25 21:07'

import xadmin
from .models import EmailVerifyRecord, Banner




class EmailVerifyRecordAdmin(object):
    # code = models.CharField(max_length=20, verbose_name=u"验证码")
    # # 如果不指定null=True 默认是不能为null
    # email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # send_type = models.CharField(verbose_name=u"验证码类型", choices=(("register", u"注册"), ("forget", u"忘记密码")),
    #                              max_length=30)
    # # 注意;这里datetime.now()去掉括号,防止以保存的时间作为时间
    # # 注意 如果这里不加verbose_name="xxx" 那么在页面上就会展示英文名字 send_time
    # send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)
    # 元组中只有一个元素时.需要在后面加上 , 号
    list_display = ['code', 'email', 'send_time', 'send_type']
    # 列表内是搜索的字段,时间search很复杂,所以去掉时间字段
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_time', 'send_type']
    pass


class BannerAdmin(object):
    # title = models.CharField(max_length=100, verbose_name=u"标题")
    # image = models.ImageField(max_length=100, upload_to="banner/%Y/%m", verbose_name=u"轮播图")
    # url = models.URLField(max_length=200, verbose_name=u"访问地址")
    # index = models.IntegerField(default=100, verbose_name=u"顺序")
    # add_time = models.DateTimeField(default=datetime.no

    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 列表内是搜索的字段,时间search很复杂,所以去掉时间字段
    search_fields = ['title', 'image', 'url', 'index']
    # 过滤
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    pass



# 注册模型
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


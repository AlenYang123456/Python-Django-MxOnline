#coding=utf-8
#!/usr/bin/ env python
from .views import OrgView, AddUserAskView, OrgHomeView

__author__ = 'AllenQ'
__date__ = '22:08'

from django.conf.urls import url, include

urlpatterns=[
    url(r'^list/$', OrgView.as_view(),name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(),name="add_ask"),
    url(r'^home/(?P<org_id>\d+)$', OrgHomeView.as_view(),name="home"),
]


# coding=utf-8
# !/usr/bin/ env python
import xadmin
from .models import CityDict, CourseOrg, Teacher

__author__ = 'AllenQ'
__date__ = '23:19'
from xadmin import views


# xadmin主题设置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
class GlobalSetting(object):
    # 固定属性
    site_title = "杨强的代码小屋"
    site_footer = "com.yq.luck"
    menu_style="accordion" #固定值 收器左侧栏
# 注册主题
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(views.CommAdminView, GlobalSetting)

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    model_icon = "fa fa-weibo"
    pass


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums']
    # relfield_style = 'fk-ajax'
    # style_fields = {"desc": "ueditor"}
    # model_icon = 'fa fa-university'
    model_icon = 'fa fa-user-md'


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']
    model_icon = 'fa fa-user-md'


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)


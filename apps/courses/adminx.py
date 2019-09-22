#coding=utf-8
#!/usr/bin/ env python
import xadmin

__author__ = 'AllenQ'
__date__ = '21:35'
from .models import Course,Lesson,Video,CourseResource

class CourseAdmin(object):
    # name = models.CharField(max_length=100, verbose_name=u"课程名称")
    # desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    # # TextField支持的字符数多
    # detail = models.TextField(verbose_name=u"课程详情")
    # degree = models.CharField(verbose_name=u"课程难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    # learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    # students = models.IntegerField(default=0, verbose_name=u"学习人数")
    # fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    # image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"课程图片")
    # click_nums = models.IntegerField(verbose_name=u"课程点击数", default=0)
    # add_time = models.DateTimeField(default=datetime.now, v
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    pass

class LessonAdmin(object):
    # course = models.ForeignKey(Course, verbose_name=u"课程")
    # name = models.CharField(max_length=100, verbose_name=u"章节名称")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    # Admin中的外键如何处理
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    pass


class CourseResourceAdmin(object):
    # course为外键
    list_display = ['course', 'name', 'download','add_time']
    search_fields = ['course', 'name','download']
    # 指定显示为外键的模型的name字段
    list_filter = ['course__name', 'name', 'download','add_time']
    pass


xadmin.site.register(CourseResource,CourseResourceAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Course,CourseAdmin)

# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from organization.models import CourseOrg

# Create your models here.

class Course(models.Model):
    """定义课程模型"""
    # 注意 添加外键的时候,要允许为空,不然在添加的时候会出很多问题
    course_org=models.ForeignKey(CourseOrg,verbose_name="课程机构",null=True)
    name = models.CharField(max_length=100, verbose_name=u"课程名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    # TextField支持的字符数多
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(verbose_name=u"课程难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"课程图片")
    click_nums = models.IntegerField(verbose_name=u"课程点击数", default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """定义章节模型 """
    # 与课程是一对多关系,通过Django中的外键关联
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    pass


class Video(models.Model):
    """定义视频模型类"""
    # 与章节是一对多关系,通过Django中的外键关联
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    pass


class CourseResource(models.Model):
    """定义章节资源模型类"""
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"资源名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    pass

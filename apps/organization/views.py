# coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from organization.forms import UserAskFrom, UserAskForm1
from .models import CourseOrg, CityDict

from django.http import HttpResponse


class OrgView(View):
    """课程机构列表功能"""

    def get(self, request):
        # 全部课程机构
        all_orgs = CourseOrg.objects.all()
        # 全部城市
        all_citys = CityDict.objects.all()
        # 总数
        org_count = CourseOrg.objects.count()
        return render(request, "org-list.html", {
            "all_orgs": all_orgs, "all_citys": all_citys, "org_count": org_count
        })

    pass


class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskFrom(request.POST)
        # us=UserAskForm1(request.POST)
        if userask_form.is_valid():
            # 注意这里 使用ModelFrom校验时,会将参数放到,Model中去,因此可以直接调用
            # ModedlFroms的save方法进行保存,注意要设置提供为True
            user_ask = userask_form.save(commit=True)
            # return HttpResponse('{"status":"success"}', content_type='application/json')
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            # 校验失败
            # return HttpResponse("{'status':'fail','msg':{0}}".format(userask_form.erors))--这里错误原因不明白
            return HttpResponse('{"status":"fail","msg":"添加出错"}',
                                content_type='application/json')
            # return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')

class OrgHomeView(View):
    """
    机构首页
    """
    def get(self,request,org_id):
        print(org_id)
        print(type(org_id))
        course_org=CourseOrg.objects.get(id=org_id)
         #取出课程机构中的外键 格式 课程对象.外键小写_set.all()
        all_courses=course_org.course_set.all()[:3]
        all_teachers=course_org.teacher_set.all()[:1]
        return render(request,'org-detail-homepage.html',{
            'all_courses':all_courses,
            'all_teachers':all_teachers
        })
        pass
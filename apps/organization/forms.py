# coding=utf-8
# !/usr/bin/ env python
from django import forms

from operation.models import UserAsk
import re

__author__ = 'AllenQ'
__date__ = '22:25'


class UserAskForm1(forms.Form):
    """普通的From"""
    pass


class UserAskFrom(forms.ModelForm):
    """模型表单的From==>>ModelForm"""

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """校验mobile:格式必须为clean_mobile,在views中实例化的该表单的时候会自动调用"""
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")

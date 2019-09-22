# coding=utf-8
from random import Random

from users.models import EmailVerifyRecord
from django.core.mail import send_mail
# 导入settings文件里面的
from MxOnline.settings import EMAIL_FROM
def send_register_eamil(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title="暮雪在线网注册激活连接"
        email_body="请点击下面的连接激活你的账号 :http//127.0.0.1:8000/active/{}".format(code)
        # django提供的方法mail方法 参数1,标题,参数2,信息,参数3 发件人邮件, 参数4,注册邮件
        send_status=send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass
    elif send_type=="forget":
        email_title="暮雪在线网忘记密码连接"
        email_body="请点击下面的连接找回你的账号 :http//127.0.0.1:8000/reset/{}".format(code)
        # django提供的方法mail方法 参数1,标题,参数2,信息,参数3 发件人邮件, 参数4,注册邮件
        send_status=send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass
        pass


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

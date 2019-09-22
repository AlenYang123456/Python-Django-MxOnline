from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
# django 提供的认证的方法
from django.contrib.auth import authenticate, login
# Create your views here.
from django.views.generic import View

from users.forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from users.models import UserProfile, EmailVerifyRecord
from utils.email_send import send_register_eamil


class IndexView(View):
    """首页视图"""
    def get(self, request):
        return render(request, "index.html", {})




class ForgetPwdView(View):
    """忘记密码视图"""
    def get(self,request):
        # 这一步是为什么???????
        forget_form=ForgetPwdForm()
        return render(request,"forgetpwd.html",{"forget_form":forget_form})
        pass
    def post(self,request):
        """表单提交的方法"""
        forget_form=ForgetPwdForm(request.POST)
        if forget_form.is_valid:
            email=request.POST.get("email","")
            send_register_eamil(email,"forget")
            return render(request,"send_success.html")
        else:
            return render(request,"forgetpwd.html",{"forget_form":forget_form})
        pass


class ActiveUserView(View):
    """用户邮箱激活的视图函数"""

    def get(self, request, active_code):
        # 先查找激活码是否存在数据中库
        all_record = EmailVerifyRecord.objects.filter(active_code=active_code)
        for record in all_record:
            email = record.email
            user = UserProfile.objects.get(email=email)
            # 修改激活状态
            user.is_active = True
        return render(request, "login.html")


class RegisterView(View):
    """注册页面的视图--基于类的视图"""

    def get(self, request):
        # register_form=RegisterForm(request.POST)
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")  # email
            pass_word = request.POST.get("password", "")  # 密码

            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            # 注册的账号的初始激活状态都应该是未激活
            user_profile.is_active = False
            user_profile.save()
            # 发送邮件
            send_register_eamil(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})

    pass


class LoginView(View):
    """基于类的视图--基于类的视图"""
    def post(self, request):
        """重写post方法,不用判断get还是post方法了"""
        login_form = LoginForm(request.POST)
        # 后端的表单校验--防君子 不方小人
        if login_form.is_valid():
            # 实际上是对每个字段做了字典的验证,检查ErrorDict是否为None
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            # 使用django自带的api去验证,如果验证成功,就会返回用户模型,失败则返回None
            # 这里必须带上key username和passoword
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active is False:
                    return render(request, "login.html", {"msg": "用户未激活,请激活"})
                    # django自带的验证成功后的登录方法login,参数1 request;参数2 用户
                    # 注意 这个django的login 和方法的login不能定义一样,否则会报错
                login(request, user)
                # 跳转到首页
                return render(request, "index.html")
        else:
            # 登录失败,需要有好提示,携带msg消息给前端,这里传递login_error 对象 给前端,前端通过errors属性取值
            #     return render(request, "login.html", {"msg": "用户名或者密码错误","login_error":login_form})
            return render(request, "login.html", {"login_error": login_form})

    def get(self, request):
        """重写get方法,,不用判断get还是post方法了"""
        return render(request, "login.html", {"msg": "用户名或者密码错误"})



class ResetView(View):
    """重置密码的视图"""
    def get(self, request, active_code):
        """携带url请求"""
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email":email})
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class ModifyPwdView(View):
    """
    修改用户密码的视图
    """
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email":email, "msg":"密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()

            return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email":email, "modify_form":modify_form})

class CustomBackend(ModelBackend):
    """重写鉴权的方法"""

    # 这里定义这个类继承ModelBackend 重写authenticate()方法
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 注意 get 是取一个 all是取所有
            # 方法一.通过username 去数据库校验
            # user = UserProfile.objects.get(username=username)
            # Q的语法 用于求并集,.get(Q(username=username)|Q(emial=username),gender=username)
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # 注意django中密码存的是密文,拿出来也无法比较,只能通过特殊api去取
            if user.check_password(password):
                return user
        except Exception as e:
            return None
            pass


def user_login(request):
    """用户登录的方法---基于方法的视图"""
    if request.method == "POST":
        # 取到post中的数据 .get("名称","默认值")
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        # 使用django自带的api去验证,如果验证成功,就会返回用户模型,失败则返回None
        # 这里必须带上key username和passoword
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            if user.is_active is False:
                return render(request, "login.html", {"msg": "用户未激活,请激活"})
            # django自带的验证成功后的登录方法login,参数1 request;参数2 用户
            # 注意 这个django的login 和方法的login不能定义一样,否则会报错
            login(request, user)
            # 跳转到首页
            return render(request, "index.html")
        else:
            # 登录失败,需要有好提示,携带msg消息给前端
            return render(request, "login.html", {"msg": "用户名或者密码错误"})
        pass
    elif request.method == "GET":
        return render(request, "login.html")
    pass

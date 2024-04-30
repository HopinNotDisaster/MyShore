from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator

# from .forms import *
# from django.http import HttpResponse
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature
from django.contrib.auth import login as lgi, logout as lgo, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import CustomUser
from operate.models import UserCollects


# Create your views here.

#
def regist(req):
    errors = None
    rf = RegistForm(req.POST)
    # 点击注册按钮之后干的事！
    if req.method == "POST":
        # 使用前端传入的数据 创建一个带有数据的表单

        if rf.is_valid():
            # 模型中没有重复密码字段 需要删除
            password2 = rf.cleaned_data.pop("password2")
            password = rf.cleaned_data["password"]
            if password2 != password:
                errors = """
                    <ul class="errorlist"><li>密码<ul class="errorlist"><li>密码不一致。</li></ul></li></ul>
                """
            else:
                # 获取用户实例  但是没有保存数据库 （密码没加密）
                new_user = rf.save(commit=False)
                # 对用于密码加密
                new_user.password = make_password(new_user.password)
                # 控制账户未激活
                new_user.is_active = False
                # # 保存数据库
                # rf.save()
                new_user.save()


                # 不能发送超级连接
                # user.email_user("激活邮件", "<a href='https://www.baidu.com'>点我激活</a>")
                print(settings.SECRET_KEY)
                seria = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY)
                seria_id = seria.dumps({
                    "id": new_user.id
                }).decode()
                # 发送带有富文本邮件
                msg = EmailMultiAlternatives("点我可以激活你的账号！", to=[new_user.email, ])
                msg.attach_alternative(f"<a href='http://localhost:8888/user/active/{seria_id}'>点我激活</a>",
                                       "text/html")
                msg.send()
                return HttpResponse("123")

        else:
            errors = rf.errors

    # 刚进入注册页面
    # 创建空表单传入模板 通过传入req.POST 可以保留原始记录 就是你输入错误之后你的用户名不需要二次输入！
    return render(req, "user/regist.html", locals())


def active(req, id):
    seria = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY, expires_in=60)
    try:
        seria_id = seria.loads(id)
    except SignatureExpired:
        return HttpResponse("超时！")
    uid = seria_id["id"]
    die_user = get_object_or_404(CustomUser, pk=uid)
    die_user.is_active = True
    die_user.save()
    return redirect(reverse("use:login"))


def login(req):
    if req.method == "POST":
        lf = LoginForm(req.POST)
        if lf.is_valid():
            username = lf.cleaned_data["username"]
            password = lf.cleaned_data["password"]
            # user = authenticate(req,username,password)
            user = CustomUser.objects.filter(username=username)[0]
            if user:
                if user.check_password(password):
                    if user.is_active:
                        lgi(req, user)
                        return redirect(reverse("main:index"))
                else:
                    errors = """
                                        <ul class="errorlist"><li>密码<ul class="errorlist"><li>密码不正确。</li></ul></li></ul>
                                    """
            else:
                errors = """
                                    <ul class="errorlist"><li>用户名<ul class="errorlist"><li>用户名不存在。</li></ul></li></ul>
                                """
    lf = LoginForm(data=req.POST)
    return render(req, "user/login.html", locals())


def logout(req):
    print("当前用户退出了！！！！！！！！！！！！！！！！！！！！！！！！！！")
    lgo(req)
    return redirect(reverse("main:index"))


@method_decorator(login_required, name='dispatch')
class CenterView(TemplateView):

    # def get_template_names(self):
    #     return 'user/center.html'

    template_name = 'user/center.html'

    def get_context_data(self, **kwargs, ):
        return {
            "router_path": self.request.path.split("/")[2],
            "req": self.request
        }





@login_required()
def updateuserinfo(req):
    if req.method == "POST":
        # 使用表单数据data  更改数据库以后得instance  files 指表单中文件数据
        # 配合enctype="multipart/form-data"使用
        uif = UpdateUserInofForm(data=req.POST, files=req.FILES,  instance=req.user)
        if uif.is_valid():
            uif.save()
            # 向下次请求传入消息
            messages.success(req, '恭喜你，修改成功')
            return redirect(reverse("user:updateuserinfo"))
        else:
            errors = uif.errors
    router_path= req.path.split("/")[2]
    # data 表单提交数据  instance 数据库已有数据
    uf = UpdateUserInofForm(instance=req.user)
    return render(req, "user/updateuserinfo.html", locals())
    # return HttpResponse("更改用户信息！")


@login_required()
def updateuserpassword(req):
    router_path = req.path.split("/")[2]
    if req.method == "POST":
        pf = UpdateUserPasswordForm(data=req.POST)
        if pf.is_valid():
            password_old = pf.cleaned_data["password_old"]
            password = pf.cleaned_data["password"]
            password2 = pf.cleaned_data["password2"]

            if req.user.check_password(password_old):
                if password != password2:
                    errors = """
                            <ul class="errorlist"><li>密码错误<ul class="errorlist"><li>密码不一致。</li></ul></li></ul>
                        """
                else:
                    req.user.set_password(password)
                    req.user.save()
                    lgi(req, req.user)
                    messages.success(req, "密码修改成功")
                    return redirect(reverse("main:index"))
            else:
                errors = """
                        <ul class="errorlist"><li>原始密码<ul class="errorlist"><li>原始密码错误。</li></ul></li></ul>
                    """
        else:
            errors = pf.errors

    pf = UpdateUserPasswordForm()
    return render(req, "user/updateuserpassword.html", locals())
    # return HttpResponse("更改用户密码！")


def collects(req):
    router_path = req.path.split("/")[2]
    wallpapers = UserCollects.objects.filter(user=req.user)
    return render(req, "user/collects.html", locals())

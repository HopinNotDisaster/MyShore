from django import forms
from .models import *
# from captcha.fields import CaptchaField


class RegistForm(forms.ModelForm):
    # 在Django中，表单字段可以使用小部件（widget）来定义其在 HTML 表单中的呈现方式。
    password2 = forms.CharField(label="重复密码", widget=forms.PasswordInput(attrs={
        # form-control这个类是booststrap里面的一个类，调整样式用的！
        "class": "form-control",
        "placeholder": "再次输入密码"
    }))

    class Meta:
        model = CustomUser
        fields = ("username", "password", "email", )

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "输入用户名"
            }),
            "password": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "输入密码"
            }),
            "email": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "输入邮箱"
            })
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "输入用户名"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "输入密码"
    }))
    # captcha = CaptchaField()


class UpdateUserInofForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("head", "email",)

        widgets = {

            "head": forms.FileInput(attrs={
                "class": "form-control",

            }),
            "email": forms.TextInput(attrs={
                "class": "form-control",
            }),

        }


class UpdateUserPasswordForm(forms.Form):
    password_old = forms.CharField(label="原始密码!", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "输入原始密码"
    }))

    password = forms.CharField(label="新密码!", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "输入新密码"
    }))

    password2 = forms.CharField(label="确认密码!", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "再次输入密码"
    }))

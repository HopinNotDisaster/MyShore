from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # nick = models.CharField("昵称", max_length=20, null=True, blank=True)
    user_type = models.CharField("用户类型", max_length=1, choices={
        "0": "普通用户",
        "1": "会员",
    }, default="0")
    uid = models.CharField("用户id", max_length=15, default=0000000000)
    head = models.ImageField("头像", upload_to="head", default="head/default.png")
    email = models.EmailField(("email address"), unique=True)

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from main.models import Wallpaper
from user.models import CustomUser
from .models import UserCollects


# Create your views here.

# post请求不是都要csrf嘛，这个装饰器可以让该视图函数，不需要csrf！
@csrf_exempt
def add(req):
    if req.method == "POST":
        print("收到js发来的post添加收藏的请求！")
        w_id = req.POST.get("w")
        user_id = req.POST.get("user")
        recoed = UserCollects.objects.filter(user=user_id, wallpaper=w_id).first()
        if not recoed:
            uc = UserCollects()
            uc.user = get_object_or_404(CustomUser, pk=user_id)
            uc.wallpaper = get_object_or_404(Wallpaper, pk=w_id)
            uc.save()
            return JsonResponse({
                "code": 0,
                "info": "添加成功！"
            })
        else:
            return JsonResponse({
                "code": 1,
                "info": "已经添加过收藏了！无需添加！"
            })
    return JsonResponse({
        "code": 2,
        "info": "您发起的不是post请求！！"
    })

@csrf_exempt
def cancel(req):
    if req.method == "POST":
        print("收到js发来的post取消收藏的请求！")
        w_id = req.POST.get("w")
        user_id = req.POST.get("user")
        recoed = UserCollects.objects.filter(user=user_id, wallpaper=w_id).first()
        if recoed:
            recoed.delete()
            return JsonResponse({
                "code": 0,
                "info": "取消收藏成功！！"
            })
        else:
            return JsonResponse({
                "code": 1,
                "info": "本就没有收藏！"
            })
    return JsonResponse({
        "code": 2,
        "info": "您发起的不是post请求！！"
    })

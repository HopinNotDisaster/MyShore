from django.db import models


# Create your models here.
# from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class Category(models.Model):
    title = models.CharField("分类名", max_length=50)

    def __str__(self):
        return self.title


class Size(models.Model):
    scale = models.CharField("大小", max_length=50)

    def __str__(self):
        return self.scale


class Wallpaper(models.Model):
    title = models.CharField("壁纸名", max_length=50)
    # 存贮在数据库中的是media下方的路径
    image = models.ImageField(upload_to="main_img")
    state = models.CharField("状态", max_length=1, choices={
        "0": "不可下载",
        "1": "可下载",
    }, default="1")
    create_time = models.DateTimeField("壁纸上传时间", auto_now_add=True)
    update_time = models.DateTimeField("壁纸更新时间", auto_now=True)
    volume = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

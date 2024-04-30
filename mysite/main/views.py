from django.http import JsonResponse
from django.shortcuts import render
import random
from django.views.generic import TemplateView
from .models import *
from django.core.paginator import Paginator, Page


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        all_sizes = Size.objects.all()
        random_sizes = random.sample(list(all_sizes), 10)
        sizel = random_sizes[:5]
        sizer = random_sizes[5:]
        is_index = False
        if self.request.path == '/':
            is_index = True

        # print(is_index, "--------")

        wallpapers = Wallpaper.objects.all()

        # 创建一个分页器需要两个参数，一个参数放所有的对象，另一个是一页展示多少个！
        paginator = Paginator(wallpapers, 9)
        # 当前页码 如过没有指定就默认为1
        page_num = self.request.GET.get("page", "1")

        page_num = int(page_num)
        # page_content 是当前页码中的内容
        page = paginator.page(page_num)
        page_content = paginator.page(page_num).object_list  # 都可以得到这一页的对象

        # total_pages = paginator.num_pages

        # 获取页码范围
        page_range = paginator.page_range
        # page_range = page_content.paginator.get_elided_page_range()

        return {
            "categorys": Category.objects.all(),
            # "wallpapers": wallpapers,

            "page_num": page_num,
            "page_num_next": page_num + 1,
            "page_num_prev": page_num - 1,
            # "page_num_max": page_range[-1],

            'page_content': page_content,
            "page_range": page_range,

            "page": page,

            'is_index': is_index,

            'sizel': sizel,
            'sizer': sizer
        }


class DetailView(TemplateView):
    template_name = "main/detail.html"

    def get_context_data(self, **kwargs):
        all_sizes = Size.objects.all()
        random_sizes = random.sample(list(all_sizes), 10)
        sizel = random_sizes[:5]
        sizer = random_sizes[5:]
        all_categorys = Category.objects.all()
        random_categorys = random.sample(list(all_categorys), 4)
        # all_sizes = Size.objects.all()
        # random_sizes = random.sample(list(all_sizes), 4)
        all_ws = Wallpaper.objects.all()
        random_ws = random.sample(list(all_ws), 9)

        return {
            "wid": kwargs.get("id"),
            "w": Wallpaper.objects.filter(id=kwargs.get("id"))[0],
            "random_categorys": random_categorys,
            'sizel': sizel,
            'sizer': sizer,
            "random_ws": random_ws
        }


class CategoryView(TemplateView):
    template_name = "main/category.html"

    def get_context_data(self, **kwargs):
        # all_sizes = Size.objects.all()
        # random_sizes = random.sample(list(all_sizes), 10)
        # sizel = random_sizes[:5]
        # sizer = random_sizes[5:]
        cid = kwargs.get("id")
        ws = Wallpaper.objects.filter(category=cid)

        return {
            "cid": kwargs.get("id"),
            "c": Category.objects.filter(id=kwargs.get("id"))[0],
            # 'sizel': sizel,
            # 'sizer': sizer,
            'ws': ws
        }


class SizeView(TemplateView):
    template_name = "main/size.html"

    def get_context_data(self, **kwargs):
        all_sizes = Size.objects.all()
        random_sizes = random.sample(list(all_sizes), 10)
        sizel = random_sizes[:5]
        sizer = random_sizes[5:]
        return {
            "sid": kwargs.get("id"),
            "s": Size.objects.filter(id=kwargs.get("id"))[0],
            'sizel': sizel,
            'sizer': sizer
        }


def recommond(req):
    all_ws = Wallpaper.objects.all()
    random_ws = random.sample(list(all_ws), 9)
    print("新数据已经找到")
    print("即将return给ajax")
    # print(random_ws)
    random_ws = [{"id": w.id, "image": w.image.url, "title": w.title} for w in
                 random_ws]
    for w in random_ws:
        print(w['image'])
    return JsonResponse({
        "code": 0,
        "info": "ok",
        "random_ws": random_ws
    })

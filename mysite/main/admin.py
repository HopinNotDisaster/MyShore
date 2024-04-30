from django.contrib import admin
from .models import Size, Category, Wallpaper


# Register your models here.

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Wallpaper)
class WallpaperAdmin(admin.ModelAdmin):
    # list_display = ['title', 'display_image', ]

    # def display_image(self, obj):
    #     # return f"<img src='{obj.image.url}' width='50' />"
    #     return '<img src="{}" width="100" />'.format(obj.image.url)
    #
    # display_image.allow_tags = True

    # list_display = ['title', ]

    # readonly_fields = ['display_image']
    #
    # def display_image(self, obj):
    #     return '<img src="{}" style="max-width: 300px; max-height: 300px;" />'.format(obj.image.url)
    #
    # display_image.allow_tags = True
    # display_image.short_description = 'Image Preview'
    pass

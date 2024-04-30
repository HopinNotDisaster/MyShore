from django.contrib import admin
from .models import UserCollects


# Register your models here.

@admin.register(UserCollects)
class UserCollects(admin.ModelAdmin):
    pass

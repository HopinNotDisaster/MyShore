from django.urls import path
from .views import *

app_name = "operate"

urlpatterns = [
    path("add/", add, name="add"),
    path("cancel/", cancel, name="cancel")
]

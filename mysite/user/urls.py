app_name = "user"
from django.urls import path
from .views import *

urlpatterns = [
    path('regist/', regist, name='regist'),
    path('active/<str:id>/', active, name='active'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('center/', CenterView.as_view(), name='center'),
    path('collects/', collects, name='collects'),
    path('updateuserinfo/', updateuserinfo, name='updateuserinfo'),
    path('updateuserpassword/', updateuserpassword, name='updateuserpassword'),
]

from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("category/<int:id>/", CategoryView.as_view(), name="category"),
    path("size/<int:id>/", SizeView.as_view(), name="size"),
    # path("top/<str:top_type>/", TopView.as_view(), name="top"),
    path('detail/<int:id>/', DetailView.as_view(), name="detail"),
    path('recommond/', recommond, name="recommond")
]

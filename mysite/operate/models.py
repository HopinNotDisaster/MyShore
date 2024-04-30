from django.db import models
from user.models import CustomUser
from main.models import Wallpaper


# Create your models here.


class UserCollects(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    wallpaper = models.ForeignKey(Wallpaper, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [
            ("user", "wallpaper")
        ]

    def __str__(self):
        return f"{self.user.username}收藏了{self.wallpaper.title}"

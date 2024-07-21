from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'images/{0}/{1}'.format(instance.user.username, filename)


class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    pon_img = models.ImageField(upload_to=user_directory_path, blank=True, null=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

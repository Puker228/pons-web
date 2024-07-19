from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True, null=True)
    pon_img = models.ImageField(upload_to='pons/images/%Y/%m/%d', blank=True, null=True, default='')
    pon_file = models.FileField(upload_to='pons/files/%Y/%m/%d', blank=True, null=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

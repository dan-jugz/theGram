from django.db import models
from django.utils import timezone
from datetime import datetime
from django.conf import settings 

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)
    img_name=models.CharField(max_length=50)
    caption = models.TextField()
    likes   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    created_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f'Image{self.img_name}--{self.caption}'
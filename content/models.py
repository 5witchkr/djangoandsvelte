from django.db import models
from django.utils import timezone



# Create your models here.
class Content(models.Model):
    subject = models.CharField(max_length=200, null=False, default=False)
    content = models.TextField(max_length=2000)
    category = models.CharField(max_length=24, default='All')
    image = models.TextField(null=True)
    nickname = models.CharField(max_length=24, null=False, default=False)
    latitude = models.CharField(max_length=24, null=False, default=False)#위도
    longitude = models.CharField(max_length=24, null=False, default=False)#경도
    createDate = models.DateTimeField(default=timezone.now)
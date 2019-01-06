from django.db import models
from django.utils import timezone
from django.conf import settings
from hitcount.models import HitCountMixin

import random

def user_path(instance,filename):
    from random import choice
    import string
    arr=[choice(string.ascii_letters) for _ in range(8)]
    pid=''.join(arr)
    extension=filename.split('.')[-1]

    return '%s/%s.%s' % (instance.auther.username,pid,extension)

# Create your models here.
class Add_story(models.Model,HitCountMixin):
    auther=models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    title=models.CharField(max_length=80)
    content=models.TextField()
    update_date=models.DateTimeField()
    image=models.ImageField(upload_to=user_path,blank=True)
    tumnail_image=models.ImageField(blank=True)


    def generate(self):
        self.update_date=timezone.now()
        self.save()

    def __str__(self):
        return "%s %s" %(self.title,self.update_date)

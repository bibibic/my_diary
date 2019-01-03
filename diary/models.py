from django.db import models
from django.utils import timezone
from django.conf import settings
from hitcount.models import HitCountMixin

import random

# Create your models here.
class Add_story(models.Model,HitCountMixin):
    auther=models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    title=models.CharField(max_length=80)
    content=models.TextField()
    update_date=models.DateTimeField()

    def generate(self):
        self.update_date=timezone.now()
        self.save()

    def __str__(self):
        return "%s %s" %(self.title,self.update_date)

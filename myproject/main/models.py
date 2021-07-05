from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Main(models.Model):
    name = models.TextField()
    about = models.TextField(default="-")
    fb = models.URLField(blank=True,null=True)
    tw = models.URLField(blank=True,null=True)
    yt = models.URLField(blank=True,null=True)
    def __str__(self):
        return self.name
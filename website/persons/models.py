from __future__ import unicode_literals

from django.db import models

# Create your models here.
class items(models.Model):
    skill=models.CharField(max_length=100)
    years=models.IntegerField()
    aboutu=models.TextField(max_length=200)
    country=models.CharField(max_length=2000)


    def __unicode__(self):
        return self.skill + ' - ' + self.aboutu

class subitems(models.Model):
    skilledperson=models.ForeignKey(items,on_delete=models.CASCADE)
    subject=models.CharField(max_length=10)
    rank=models.IntegerField()
    def __unicode__(self):
        return self.subject
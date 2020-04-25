from django.db import models

# Create your models here.

class Names(models.Model):
    name = models.CharField(max_length=6)
    status = models.CharField(max_length=6,default='未答辩')
    g_score = models.FloatField(default=0)
    a_score = models.FloatField(default=0)
    e_score = models.FloatField(default=0)


class GroupScore(models.Model):
    name = models.CharField(max_length=10)
    score = models.IntegerField()


class AllScore(models.Model):
    name = models.CharField(max_length=10)
    score = models.IntegerField()

class ipinfo(models.Model):
    name = models.CharField(max_length=10)
    ip = models.CharField(max_length=15)
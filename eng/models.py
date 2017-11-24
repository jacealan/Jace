from django.db import models
from django.utils import timezone

# Create your models here.
# class Word(models.Model):
#     nth = models.IntegerField()
#     date = models.DateField(default=timezone.now)
#     no1 = models.IntegerField()
#     no2 = models.IntegerField()
#     no3 = models.IntegerField()
#     no4 = models.IntegerField()
#     no5 = models.IntegerField()
#     no6 = models.IntegerField()
#     nob = models.IntegerField()
#     winmoney = models.IntegerField()
#     winco = models.IntegerField()

class Sentences(models.Model):
    sentence = models.CharField(max_length=200)
    category = models.IntegerField()
    number = models.IntegerField()
    level = models.CharField(max_length=1)

# def publish(self):
#     self.save()

def __str__(self):
    return self.title

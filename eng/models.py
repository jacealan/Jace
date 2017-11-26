from django.db import models
from django.utils import timezone

class Sentences(models.Model):
    sentence = models.CharField(max_length=200)
    category = models.IntegerField()
    number = models.IntegerField()
    level = models.CharField(max_length=1)

class Words(models.Model):
    word = models.CharField(max_length=20)
    level = models.CharField(max_length=1)

def publish(self):
    self.save()

def __str__(self):
    return self.title

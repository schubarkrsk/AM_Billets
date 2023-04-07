from django.db import models


# Create your models here.
class Feedback(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_day = models.DateField()
    phone = models.CharField(max_length=50)
    vk = models.URLField()


class TypeOfBillets(models.Model):
    title = models.CharField(max_length=50)
    cost = models.IntegerField()

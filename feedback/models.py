from django.db import models


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)
    instagram = models.URLField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} / {self.reason} / {self.phone} / {self.instagram}"


class TypeOfBillets(models.Model):
    title = models.CharField(max_length=50)
    cost = models.IntegerField()

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Honors(models.Model):
    honor_id = models.BigIntegerField()
    eventname = models.CharField(max_length=100)
    placement = models.SmallIntegerField()
    winnings = models.FloatField()
    url = models.TextField()


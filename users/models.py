from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Team(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64, unique=True)
    # players = models.ManyToManyField(User, through='Profile')


class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    game = models.CharField(max_length=100, blank=False, default='')
    username = models.CharField(max_length=100, blank=False, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)
    ingame_name = models.CharField(max_length=100, blank=False, default='')
    firstname = models.CharField(max_length=100, blank=False, default='')
    lastname = models.CharField(max_length=100, blank=False, default='')
    discordtag = models.CharField(max_length=100, blank=False, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(blank=True)
    region = models.CharField(max_length=3, default='NA', blank=True)
    shirt_size = models.CharField(max_length=3, default='L')
    # team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, default=1, blank=True)
    team = models.CharField(max_length=100, blank=False, default='No Team')
    birthday = models.DateField(default=date.today())

    def __str__(self):
        return f'{self.username} profile'

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUser(AbstractUser):
    STATUS = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator')
    )
    email = models.EmailField(unique=True)
    status = models.CharField(choices=STATUS, default='regular', max_length=100)
    description = models.TextField('THE Description', max_length=600, default='', blank= True)

    def __str__(self):
        return self.username
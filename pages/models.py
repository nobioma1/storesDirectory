from django.conf import settings
from django.db import models
import datetime
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Store(models.Model):
    storename = models.CharField(max_length=200)
    storeaddress = models.CharField(max_length=200)
    storedetails = models.TextField(default='Empty')
    storeowner = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)
    create_date = models.DateTimeField(default=datetime.datetime.now)
    stars = models.IntegerField(default=1, help_text='select 1-5 to rate')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return self.storename

    def get_absolute_url(self):
        return reverse('storedetail', args=[str(self.id)])

class Inbox(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    message = models.TextField()
    create_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.message

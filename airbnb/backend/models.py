from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Airbnb(models.Model):
    title = models.CharField(max_length=80)
    host_name = models.TextField(max_length=50)

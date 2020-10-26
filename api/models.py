
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tank(models.Model):
    tank_name = models.CharField(max_length=30, db_index=True, unique=True)
    product = models.CharField(max_length=30)
    capacity = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

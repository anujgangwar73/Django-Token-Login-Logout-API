from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name=models.CharField(max_length=50,default='')

    def __str__(self):
        return self.username
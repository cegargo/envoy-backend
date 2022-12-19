import uuid
from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    full_name = models.CharField(max_length=128)
    college = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=32)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

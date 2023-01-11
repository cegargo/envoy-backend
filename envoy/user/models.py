from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=128)
    college = models.CharField(max_length=64)
    email = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=32)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Student(models.Model):
    Name = models.CharField(max_length=128)
    Course = models.CharField(max_length=128)
    Email = models.CharField(unique=True, max_length=128)
    Password = models.CharField(max_length=32)
    DateRegistered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Email


class Faculty(models.Model):
    Name = models.CharField(max_length=128)
    Course = models.CharField(max_length=64)
    Email = models.CharField(unique=True, max_length=128)
    Password = models.CharField(max_length=32)
    PostCount = models.IntegerField(default=0)
    DateRegistered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Email

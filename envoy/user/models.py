from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=128)
    college = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=32)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Student(models.Model):
    StudentName = models.CharField(max_length=128)
    CourseEnrolled = models.CharField(max_length=128)
    StudentEmail = models.CharField(max_length=128)
    StudentPassword = models.CharField(max_length=32)
    DateRegistered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.StudentEmail


class Faculty(models.Model):
    FacultyName = models.CharField(max_length=128)
    CourseAdministered = models.CharField(max_length=64)
    FacultyEmail = models.CharField(max_length=128)
    FacultyPassword = models.CharField(max_length=32)
    NumberOfPosts = models.IntegerField(default=0)
    DateRegistered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FacultyEmail

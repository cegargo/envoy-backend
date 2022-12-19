from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=128)
    college = models.CharField(max_length=64)
    url = models.URLField(max_length=200)
    posted_date = models.DateField()

    def __str__(self):
        return self.title

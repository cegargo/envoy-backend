from django.db import models
from user.models import Faculty


class Announcement(models.Model):
    AnnouncementTitle = models.CharField(max_length=128)
    PostDateTime = models.DateTimeField(auto_now_add=True)
    AnnouncementType = models.CharField(max_length=64)
    Author = models.ForeignKey(
        Faculty, on_delete=models.CASCADE)
    NumberOfViewers = models.IntegerField(default=0)
    Duration = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.AnnouncementType


class AnnouncementContent(models.Model):
    AnnouncementID = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    Description = models.CharField(max_length=2048)
    Image = models.ImageField(max_length=2048)
    URL = models.URLField(max_length=2048)

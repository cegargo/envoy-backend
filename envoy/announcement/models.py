from django.db import models
from user.models import Faculty


def nameFile(instance, filename):
    return '/'.join(['images', str(instance), filename])


class Announcement(models.Model):
    AnnouncementID = models.AutoField(primary_key=True)
    AnnouncementTitle = models.CharField(max_length=128)
    PostDateTime = models.DateTimeField(auto_now_add=True)
    AnnouncementType = models.CharField(max_length=64)
    Author = models.ForeignKey(
        Faculty, on_delete=models.CASCADE)
    NumberOfViewers = models.IntegerField(default=0)
    Duration = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.AnnouncementID)


class AnnouncementContent(models.Model):
    AnnouncemenContentID = models.AutoField(primary_key=True)
    AnnouncementID = models.ForeignKey(
        Announcement, on_delete=models.CASCADE)
    Description = models.CharField(max_length=2048)
    Image = models.ImageField(
        upload_to=nameFile, max_length=2048, null=True, blank=True)
    URL = models.URLField(max_length=2048, blank=True)

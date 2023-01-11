from rest_framework import serializers
from announcement.models import Announcement, AnnouncementContent


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('AnnouncementTitle', 'Author', 'AnnouncementType')


class AnnouncementContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementContent
        fields = ('AnnouncementID', 'Description', 'Image', 'URL')

from django.shortcuts import render
from . models import Announcement


def index(request):
    return 'Announcement'

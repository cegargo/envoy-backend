from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from . models import Announcement


def index(request):
    return 'Announcement'

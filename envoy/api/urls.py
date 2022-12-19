from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('api', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/<int:pk>/', views.UserListRetrieveDestroyAPIView.as_view(),
         name='user-retrieve-destroy')
]

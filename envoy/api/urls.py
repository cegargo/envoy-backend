from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    # Announcement endpoints
    path('api/news/', views.AnnouncementListCreateAPIView.as_view()),
    path('api/news/<str:college>/', views.AnnouncementView.as_view()),

    # User endpoints
    # Faculty
    path('api/users/faculty/', views.FacultyListCreateAPIView.as_view()),
    path('api/users/faculty/<str:email>/',
         views.FacultyDataAPIView.as_view()),
    # Student
    path('api/users/student/', views.StudentListCreateAPIView.as_view()),
    path('api/users/student/<str:email>/', views.StudentDataAPIView.as_view()),

    # path('api/users/<str:email>/', views.UserView.as_view()),
    # path('api/users/<int:pk>/', views.UserListRetrieveDestroyAPIView.as_view(),
    #      name='user-retrieve-destroy'),

]

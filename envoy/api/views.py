# from rest_framework.views import APIView
# from rest_framework import permissions
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from user.models import User, Faculty, Student
from user.serializers import UserSerializer, FacultySerializer, StudentSerializer
from announcement.models import Announcement, AnnouncementContent
from announcement.serializers import AnnouncementSerializer, AnnouncementContentSerializer


'''
# User
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(RetrieveDestroyAPIView):
    # queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, email):
        try:
            email_obj = User.objects.get(email=email)
            return Response(UserSerializer(email_obj).data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
'''


class FacultyListCreateAPIView(ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyListRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDataAPIView(RetrieveDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

    def get(self, request, email):
        try:
            obj = Faculty.objects.get(FacultyEmail=email)
            return Response(FacultySerializer(obj).data)
        except Faculty.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentistRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDataAPIView(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, email):
        try:
            obj = Student.objects.get(StudentEmail=email)
            return Response(StudentSerializer(obj).data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


#  Annoucements
class AnnouncementView(RetrieveDestroyAPIView):
    serializer_class = AnnouncementSerializer

    def get(self, request, college):
        try:
            college_obj = Announcement.objects.filter(
                college=college)
            return Response(AnnouncementSerializer(college_obj).data)
        except Announcement.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AnnouncementListCreateAPIView(ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class AnnouncementListRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

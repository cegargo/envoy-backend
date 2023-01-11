from rest_framework import serializers
from user.models import User, Faculty, Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'college', 'email')


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('FacultyName', 'CourseAdministered',
                  'FacultyEmail', 'FacultyPassword')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('StudentName', 'CourseEnrolled',
                  'StudentEmail', 'StudentPassword')

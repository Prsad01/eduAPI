from django.shortcuts import render
from .models import Enrollment
from courses_app.models import Course
from rest_framework import viewsets
from .serializers import EnrollmentWriteSerializer, EnrollmentReadSerializer
from accounts_app.permissions import IsStudent, NoPermission, IsInstructor, InstrucatorOrStudent
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
import datetime
import time

class Enrollmentview(viewsets.ModelViewSet):
    serializer_class = EnrollmentWriteSerializer
    queryset = Enrollment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()

        if self.request.method == 'GET':
            serializer_class = EnrollmentReadSerializer

        else:
            serializer_class = EnrollmentWriteSerializer

        kwargs['context'] = {'request': self.request}
        serializer = serializer_class(*args, **kwargs)

        return serializer

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retive':
            self.permission_classes = [InstrucatorOrStudent]
        elif self.action == 'destroy':
            self.permission_classes = [NoPermission]
        else:
            self.permission_classes = [IsStudent]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        if self.request.user.role == 'student':
            return Enrollment.objects.select_related('student').filter(student=self.request.user)
        elif self.request.user.role == 'instructor':
            # self.request.user.course_set.all()
            # Course.objects.select_related('instructor').filter(instructor = self.request.user)
            return Enrollment.objects.select_related('course__instructor').filter(course__instructor = self.request.user)
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        data = {'student': request.user.id, 'course': request.data.get('course')}
        print(request.user)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': serializer.data})
        return Response({'message': serializer.errors}, status=HTTP_400_BAD_REQUEST)

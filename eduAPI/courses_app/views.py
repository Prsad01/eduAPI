from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializers

class CourserView(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    # queryset = Course.objects.all()
    queryset = Course.objects.select_related('instructor').all()
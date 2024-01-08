from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializers
from accounts_app.permissions import IsInstructor, IsStudent, NoPermission

class CourserView(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.select_related('instructor').all()

    def get_permissions(self):
        if self.request.method=="GET":
            pass
        return super().get_permissions()
from django.shortcuts import render
from .models import Enrollment
from rest_framework import viewsets
from .serializers import EnrollmentSerializer
from .permissions import IsStudent, NoPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class Enrollmentview(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        self.permission_classes = [NoPermission]
        if self.request.user.role == 'student':
            self.permission_classes = [IsStudent]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        if self.request.user.role == 'student':
            return Enrollment.objects.select_related('student').filter(student=self.request.user)
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        data = {'student':request.user.id,'course':request.data['course']}
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':serializer.data})
        return Response({'message':serializer.errors})

    # Need to work on it more just take course id and create record of enrollment
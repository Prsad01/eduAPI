from django.shortcuts import render
from .models import Assignment
from assignment_app.serializers import *
from rest_framework.response import Response
from rest_framework import viewsets
from accounts_app.permissions import InstrucatorOrStudent,IsInstructor
from rest_framework.status import HTTP_100_CONTINUE,HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED
from enrollment_app.models import Enrollment
from courses_app.models import Course
from Lesson_app.models import Lesson
from django.db.models import Subquery


class AssignmentView(viewsets.ModelViewSet):
    queryset = Assignment.objects.select_related('lesson').all()
    serializer_class = AssignmentReadSearializer 

    def get_queryset(self):
        if self.request.user.role == 'student':
            print("student called",self.request.user)
            course_ids = Course.objects.filter(enrollment__student=self.request.user).values('pk').distinct()
            lesson_ids = Lesson.objects.filter(course_id__in = Subquery(course_ids)).values('pk').distinct()
            assignment_related_to_lesson =  Assignment.objects.filter(lesson_id__in = lesson_ids)
            
        return super().get_queryset()

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        if self.request.method == 'GET':
            serializer_class=AssignmentReadSearializer
        else:
            serializer_class = AssignmentSerializer
        kwargs['context'] = {'request': self.request}
        serializer = serializer_class(*args,**kwargs)
        return serializer 
            
    def get_permissions(self):
        print(self.request.method)
        if self.request.method  == 'GET':
            self.permission_classes = [InstrucatorOrStudent]
        else:
            self.permission_classes = [IsInstructor]
            
        return [permission() for permission in self.permission_classes]
    

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
        except serializers.ValidationError as e:
            if 'code' in e.detail and e.detail['code'] == '101' and 'lesson' in e.detail:
                
                return Response({'lesson': e.detail['lesson']}, status=HTTP_401_UNAUTHORIZED)
       
            if 'code' in e.detail and e.detail['code'] == '102' and 'lesson' in e.detail:
                
                return Response({'lesson': e.detail['lesson']}, status=HTTP_401_UNAUTHORIZED)
       
        return super().create(request, *args, **kwargs)
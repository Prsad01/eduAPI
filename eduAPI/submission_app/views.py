from django.shortcuts import render
from submission_app.models import Submission
from submission_app.serializers import SubmissionSrializer
from rest_framework.response import Response
from rest_framework import viewsets
from assignment_app.models import Assignment
from enrollment_app.models import Enrollment
from Lesson_app.models import Lesson
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from .permissions import IsStudent

class SubmissionView(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSrializer
    permission_classes = [IsStudent]


    def get_queryset(self):
        return Submission.objects.select_related('student').filter(student = self.request.user)
  
    def create(self, request, *args, **kwargs):
        data = {'student':request.user.id,
                'assignment':request.data['assignment'],
                'content':request.data['content']
                }
        
        assignment = get_object_or_404(Assignment,pk=request.data['assignment'])
        lesson = get_object_or_404(Lesson,pk=assignment.lesson.id)
        student_eligible = Enrollment.objects.filter(student = request.user.id , course = lesson.course ).exists()

        if student_eligible:
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':serializer.data})
            return Response({'message':serializer.errors})
        else:
            return Response({'message':f'student is not registered for give Course - {lesson.course} and Assignment- {assignment}'})
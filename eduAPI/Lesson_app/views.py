from rest_framework.response import Response
from .serializers import LessonSerializer
from .models import Lesson
from rest_framework import generics
from accounts_app.permissions import IsStudent, IsInstructor,InstrucatorOrStudent
from enrollment_app.models import Enrollment
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404,get_list_or_404

class CreateLessonView(generics.CreateAPIView):
    # queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsInstructor]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"all lessons are added"})
        return Response({'message':serializer.errors})

class ListLessonView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [InstrucatorOrStudent]

    def list(self, request, *args, **kwargs):
        course_id = self.kwargs['course_id']
        get_list_or_404(Lesson,course_id=course_id)
         

        if self.request.user.groups.filter(name='students_group').exists():
            if Enrollment.objects.filter(student = self.request.user,course_id=course_id).exists():
                serializer = self.get_serializer(self.get_queryset(),many=True)
                return Response(serializer.data)
            else:
                return Response({'details':'You did not subscribed given course'},status=HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Lesson.objects.filter(course_id = course_id)

class LessonRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'order'

    def destroy(self, request, *args, **kwargs):
        course_id = self.kwargs['course_id']
        order = self.kwargs['order']

        if(Lesson.objects.filter(course_id = course_id,order= order).exists()):
            lesson = Lesson.objects.get(course_id = course_id,order= order)
            lesson.delete()
            return Response({'message':'Lesson deleted successfully.'})
        return Response({'message':f'Lesson {order} with course {course_id} dose not exists'})

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        order = self.kwargs['order']
        return Lesson.objects.filter(course_id = course_id,order= order)
    
from django.shortcuts import render ,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LessonSerializer
from rest_framework import viewsets
from .models import Lesson
from rest_framework import generics


class CreateLessonView(generics.CreateAPIView):
    # queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def create(self, request, *args, **kwargs):
        print("create methode called")
        # print(request.data)
        serializer = self.get_serializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"all lessons are added"})
        return Response({'message':serializer.errors})

class ListLessonView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

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
    
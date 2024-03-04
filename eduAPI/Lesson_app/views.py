from rest_framework.response import Response
from .serializers import LessonSerializer,LessonReadSerializer
from .models import Lesson
from rest_framework import generics
from accounts_app.permissions import IsStudent, IsInstructor,InstrucatorOrStudent
from enrollment_app.models import Enrollment
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404,get_list_or_404
from accounts_app.permissions import InstrucatorOrStudent,IsInstructor

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
    serializer_class = LessonReadSerializer
    permission_classes = [InstrucatorOrStudent]

    def get_queryset(self):
        print("from get queryset")
        course_id = self.kwargs['course_id']
        return Lesson.objects.filter(course_id = course_id)

    def list(self, request, *args, **kwargs):
        course_id = self.kwargs['course_id']
        get_list_or_404(Lesson,course_id=course_id)
         

        if self.request.user.groups.filter(name='students_group').exists():
            print("student")
            if Enrollment.objects.filter(student = self.request.user,course_id=course_id).exists():
                print("printing from lesson list ")
                print(self.get_queryset())
                serializer = self.get_serializer(self.get_queryset(),many=True)

                return Response(serializer.data)
            else:
                return Response({'details':'You did not subscribed given course'},status=HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)

  

class LessonRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonReadSerializer
    lookup_field = 'order'

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        order = self.kwargs['order']
        return Lesson.objects.filter(course_id = course_id,order = order)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = {'request': self.request,'course_id':self.kwargs['course_id']}
        serializer = serializer_class(*args,**kwargs)

        return serializer

    # def retrieve(self, request, *args, **kwargs):
    #     print("retrive called")
    #     course_id = self.kwargs['course_id']
    #     if self.request.user.role == 'student':
    #         if Enrollment.objects.filter(student = self.request.user,course_id=course_id).exists() :
    #             serializer = self.get_serializer(self.get_queryset(),many=True)
    #             return Response({'data':serializer.data})
    #     return super().retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print("from retrive")
        course_id = self.kwargs['course_id']
        if self.request.user.role == 'student':
            if Enrollment.objects.filter(student = self.request.user,course_id=course_id).exists():
                serializer = self.get_serializer(self.get_queryset(),many=True)
                return Response(serializer.data)
            else:
                return Response({'details':'You did not subscribed given course'},status=HTTP_400_BAD_REQUEST)
        return super().retrieve(request, *args, **kwargs)

    def get_permissions(self):
        if(self.request.method == 'GET'):
            self.permission_classes = [InstrucatorOrStudent]
        else:
            self.permission_classes = [IsInstructor]
        return [permission() for permission in self.permission_classes]
    
    def destroy(self, request, *args, **kwargs):
        course_id = self.kwargs['course_id']
        order = self.kwargs['order']

        if(Lesson.objects.filter(course_id = course_id,order= order).exists()):
            lesson = Lesson.objects.get(course_id = course_id,order= order)
            lesson.delete()
            return Response({'message':'Lesson deleted successfully.'})
        return Response({'message':f'Lesson {order} with course {course_id} dose not exists'})

   
    
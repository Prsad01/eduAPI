from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializers, CourseReadSerializers
from accounts_app.permissions import IsInstructor, IsStudent, NoPermission, InstrucatorOrStudent
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response


class CourserView(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.select_related('instructor').all()
    permission_classes = [IsInstructor,IsAuthenticated]
    

    def destroy(self, request, *args, **kwargs):
        course = self.get_object()
        if (course.instructor == request.user):
            return Response({'details':f' {course} deleted successfully'})
        return Response({'details':f'Not eligible'})
 
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        if self.request.method == 'GET':
            serializer_class = CourseReadSerializers
        elif self.request.method == 'POST':
            serializer_class = CourseSerializers
        kwargs['context'] = {'request': self.request}
        serializer = serializer_class(*args,**kwargs)
        return serializer   

    def get_permissions(self): 
        print("from course permission")
        if self.action == 'list' or self.action == 'retrieve':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsInstructor]

        return [permission() for  permission in self.permission_classes]  
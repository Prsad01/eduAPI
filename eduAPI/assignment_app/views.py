from django.shortcuts import render
from .models import Assignment
from assignment_app.serializers import *
from rest_framework.response import Response
from rest_framework import viewsets
from accounts_app.permissions import InstrucatorOrStudent,IsInstructor
from rest_framework.status import HTTP_100_CONTINUE,HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED

class AssignmentView(viewsets.ModelViewSet):
    queryset = Assignment.objects.select_related('lesson').all()
    serializer_class = AssignmentReadSearializer 

    def get_serializer(self, *args, **kwargs):
        # print("from get serializer")
        # print(kwargs)
        serializer_class = self.get_serializer_class()
        if self.request.method == 'GET':
            serializer_class=AssignmentReadSearializer
        else:
            serializer_class = AssignmentSerializer
        kwargs['context'] = {'request': self.request}
        serializer = serializer_class(*args,**kwargs)
        return serializer 
            
    def get_permissions(self):
        if self.request == 'GET':
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
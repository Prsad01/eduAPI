from django.shortcuts import render
from .models import Assignment
from .serializers import AssignmentSerializer
from rest_framework.response import Response
from rest_framework import viewsets

class AssignmentView(viewsets.ModelViewSet):
    queryset = Assignment.objects.select_related('lesson').all()
    serializer_class = AssignmentSerializer
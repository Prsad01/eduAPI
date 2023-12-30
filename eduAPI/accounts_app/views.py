from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def partial_update(self, request, *args, **kwargs):
        instannce = self.get_object()
        serialier = self.get_serializer(instannce,data=request.data,partial=True)
        serialier.is_valid(raise_exception=True)
        serialier.save()
        return Response(serialier.data)
from .serializers import ReviewWriteSerializer,ReviewReadSerializer
from .models import Review
from rest_framework import viewsets
from rest_framework.response import Response
from accounts_app.permissions import IsInstructor,IsStudent,NoPermission
from submission_app.models import Submission

class Review_view(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewWriteSerializer
    permission_classes = [NoPermission]

    def get_permissions(self):
        if self.request.user.role == "instructor":
            self.permission_classes = [IsInstructor]
        elif self.request.user.role == "student":
            self.permission_classes = [IsStudent]
        return [permission() for  permission in self.permission_classes]

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        if self.request.method == 'GET':
            serializer_class = ReviewReadSerializer
        elif self.request.method == 'POST':
            serializer_class = ReviewWriteSerializer
        kwargs['context'] = {'request': self.request}
        serializer = serializer_class(*args,**kwargs)
        return serializer
    
    def get_queryset(self):
        if self.request.user.role=="instructor":
            return Review.objects.filter(instructor = self.request.user)
        elif self.request.user.role=="student":
            sub = Submission.objects.filter(student = self.request.user)
            print(Review.objects.filter(submission__in = sub).count())
            return Review.objects.filter(submission__in = sub)
        return super().get_queryset()

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Enrollmentview

router = DefaultRouter(trailing_slash=False)
router.register('',Enrollmentview,basename='Enrollment')

urlpatterns = [
]+router.urls

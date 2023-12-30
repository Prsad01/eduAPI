from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CourserView

router = DefaultRouter(trailing_slash=False)

router.register('',CourserView,basename='courses')

urlpatterns = [
 
]+router.urls

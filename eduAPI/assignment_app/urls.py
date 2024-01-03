from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AssignmentView

router = DefaultRouter(trailing_slash=False)
router.register('',AssignmentView,basename='Assiggnment')

urlpatterns = [
]+router.urls

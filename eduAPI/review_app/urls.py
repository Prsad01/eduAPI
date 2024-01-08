from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Review_view

router = DefaultRouter()
router.register('',Review_view,basename='Review')

urlpatterns = [
]+router.urls

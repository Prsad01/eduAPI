from django.urls import path,include
from rest_framework.routers import DefaultRouter
from submission_app.views import SubmissionView

router = DefaultRouter(trailing_slash=False)
router.register('',SubmissionView,basename ='Submission')

urlpatterns = [
]+router.urls

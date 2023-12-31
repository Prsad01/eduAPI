from django.urls import path,include
from .views import CreateLessonView, ListLessonView, LessonRetriveUpdateDestroyView


urlpatterns = [
    path('course/lesson',CreateLessonView.as_view(),name='lesson-create'),
    path('course/<int:course_id>/lesson',ListLessonView.as_view(),name="lesson-list"),
    path('course/<int:course_id>/lesson/<int:order>',LessonRetriveUpdateDestroyView.as_view(),name='lesson-DeleterRetriveUpdate'),
]

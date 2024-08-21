from django.contrib import admin
from .models import Course
# Register your models here.


class LessonModelAdmin(admin.ModelAdmin):
    list_display=['id','title','instructor']


admin.site.register(Course,LessonModelAdmin)
from django.contrib import admin
from .models import Lesson


class LessonModelAdmin(admin.ModelAdmin):
    list_display=['id','course','order','title']
    

admin.site.register(Lesson,LessonModelAdmin)
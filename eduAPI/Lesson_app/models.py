from django.db import models
from courses_app.models import Course

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.IntegerField() # order field is for probiding a sequeance no for each lesson
    # video_url = models.URLField()

    def __str__(self):
        return self.title

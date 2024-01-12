from django.db import models
from Lesson_app.models import Lesson
 
class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    max_score = models.PositiveIntegerField()

    def __str__(self):
        return self.title
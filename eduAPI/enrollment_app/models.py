from django.db import models
from accounts_app.models import User
from courses_app.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"
    
    class Meta:
        unique_together = ['student','course']
from django.db import models
from accounts_app.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'role': 'instructor'},db_index=True)
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return self.title
    

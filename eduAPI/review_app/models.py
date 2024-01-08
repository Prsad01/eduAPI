from django.db import models
from submission_app.models import Submission
from accounts_app.models import User

class Review(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE , limit_choices_to={'role': 'instructor'})
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE,related_name='review')
    score = models.PositiveIntegerField()
    feedback = models.TextField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.instructor.username} for {self.submission.assignment.title}"

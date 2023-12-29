from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(unique=True)
    ROLES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='student')
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)


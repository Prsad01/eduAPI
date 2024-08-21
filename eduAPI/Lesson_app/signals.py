from Lesson_app.models import Lesson
from enrollment_app.models import Enrollment
from accounts_app.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save




@receiver(post_save, sender=Lesson)
def notify_new_lesson(sender, instance, created, **kwargs):
    if created:
        print("New lesson created")
        print(instance)
    else:
        print("Lesson updated")

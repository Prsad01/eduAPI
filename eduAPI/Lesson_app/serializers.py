from rest_framework import serializers
from .models import Lesson
from rest_framework.validators import UniqueTogetherValidator

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['course','order','title','content','id' ]

        validators = [
            UniqueTogetherValidator(
                queryset= Lesson.objects.all() ,
                fields = ('course','order'),
                message = "The lesson for given course is already there"
             )
        ]
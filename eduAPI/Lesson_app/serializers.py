from rest_framework import serializers
from .models import Lesson
from rest_framework.validators import UniqueTogetherValidator
from courses_app.models import Course
from courses_app.serializers import CourseReadSerializers

class LessonReadSerializer(serializers.ModelSerializer):
    course = CourseReadSerializers()
    class Meta:
        model = Lesson
        fields = ['id','course','order','title','content','id' ]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id','course','order','title','content','id' ]

        validators = [
            UniqueTogetherValidator(
                queryset= Lesson.objects.all() ,
                fields = ('course','order'),
                message = "The lesson for given course is already there"
             )
        ]

    def update(self, instance, validated_data):
        instructor = self.context['request'].user
        courseID = self.context['course_id']

        if (Course.objects.select_related('instructor').filter(instructor=instructor,pk=courseID).exists()):

            instance.order = validated_data.get('order')
            instance.title = validated_data.get('title')
            instance.content = validated_data.get('content')
            instance.save()
          
        else:
            raise serializers.ValidationError({'details':F'{instructor} is not belongs to given course  '})
        
        return instance 
from .models import Assignment
from rest_framework import serializers
from Lesson_app.serializers import LessonReadSerializer
from Lesson_app.models import Lesson
from django.shortcuts import get_object_or_404
from courses_app.models import Course

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"
        
    def check_authority(request,lesson):
        request_user = request.user

        lesson_course = Lesson.objects.get(pk=lesson.id)
        return (Course.objects.filter( pk=lesson_course.course.id,instructor=request_user).exists())
    
    # def update(self, instance, validated_data):
    #     print("update called")
    #     if not AssignmentSerializer.check_authority(self.context['request'],lesson):
    #         raise serializers.ValidationError({'lesson':'You are not authorised to update Assignment for given Lesson','code':'102'})
    #     return instance


    def create(self, validated_data):
        lesson = validated_data.get('lesson')

        if not AssignmentSerializer.check_authority(self.context['request'],lesson):
            raise serializers.ValidationError({'lesson':'You are not authorised to add Assignment for given Lesson','code':'101'})
       
        # assignment  = Assignment(
        #     title = validated_data.get('title'),
        #     description = validated_data.get('description'),
        #     due_date = validated_data.get('due_date'),
        #     lesson_id = validated_data.get('lesson').id,
        #     max_score = validated_data.get('max_score')
        #     )
        assignment  = Assignment(**validated_data)
        # assignment.save()  
        return assignment

class AssignmentReadSearializer(serializers.ModelSerializer):
    lesson = LessonReadSerializer()
    class Meta:
        model = Assignment
        fields = "__all__"
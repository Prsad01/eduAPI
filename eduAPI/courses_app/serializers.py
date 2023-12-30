from rest_framework import serializers
from .models import Course
from accounts_app.models import User
from accounts_app.serializer import UserSerializer
from django.shortcuts import get_object_or_404

class CourseSerializers(serializers.ModelSerializer):
    instructor = serializers.CharField(source='instructor.username')
    email = serializers.CharField(source='instructor.email' , read_only=True)
    class Meta:
        model = Course
        fields = ['id','title','description','instructor','email','start_date','end_date']


    def validate_instructor(self,value):
        try:
            user = User.objects.get(pk=value)
            if (user.role != 'instructor'):
                raise serializers.ValidationError({'details': f'instructor with id {value} not found'})
        except User.DoesNotExist:
            raise serializers.ValidationError({'details': f'user with id {value} not found'}) 
        return value
    
    def update(self, instance, validated_data):
        # print(validated_data)
        title = validated_data.get('title')
        description = validated_data.get('description')
        instructor = validated_data.get('instructor')
        start_date = validated_data.get('start_date')
        end_date = validated_data.get('end_date')
      
        if instructor is not None:
            instance.instructor_id = instructor['username']
        if title is not None:
            instance.title = title
        if description is not None:
            instance.descrption = description
        if start_date is not None:
            instance.start_date = start_date
        if end_date is not None:
            instance.end_start = end_date
        instance.save()
        return instance
 
    def create(self, validated_data):
        title = validated_data.pop('title')
        description = validated_data.pop('description')
        instructor = validated_data.pop('instructor')
        start_date = validated_data.pop('start_date')
        end_date = validated_data.pop('end_date')
       
        course = Course(
            title=title,
            description = description,
            instructor_id = instructor['username'],
            start_date = start_date,
            end_date =end_date)
        course.save()                     
        return course
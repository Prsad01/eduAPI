from .models import Submission
# from assignment_app.models import Assignment
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from accounts_app.serializer import UserSerializerWithLimitedFields
from assignment_app.serializers import AssignmentSerializer

class SubmissionSerializerForRead(serializers.ModelSerializer):
     student = UserSerializerWithLimitedFields()
     assignment = AssignmentSerializer()
     class Meta:
          model = Submission
          fields = ('id','student','assignment','content','submission_date','feedback')


class SubmissionSrializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"
    
    validators = [
        UniqueTogetherValidator(
            queryset = Submission.objects.all(),
            fields=('student','assignment'),
            message='student already subimted the assignment'
        )
    ]
    
    def update(self, instance, validated_data):
        print(validated_data.keys())
        if 'student' in validated_data.keys():
            raise serializers.ValidationError({'message':'you can only update Feedback and content fields not student'})
        elif 'assignment' in validated_data.keys():
              raise serializers.ValidationError({'message':'you can only update Feedback and content fields not assignment'})
        elif 'submission_date' in validated_data.keys():
              raise serializers.ValidationError({'message':'you can only update Feedback and content fields not submission_date'})
        
 
        instance.content = validated_data.get('content')
        instance.feedback = validated_data.get('feedback')
        instance.save()
        return instance
        return super().update(instance, validated_data)
    
from rest_framework import serializers
from .models import Review
from submission_app.models import Submission
from assignment_app.models import Assignment
from Lesson_app.models import Lesson
from courses_app.models import Course
from rest_framework.validators import UniqueTogetherValidator
from accounts_app.serializer import UserSerializerWithLimitedFields
from submission_app.serializers import SubmissionSerializerForRead
from django.shortcuts import get_object_or_404

class ReviewReadSerializer(serializers.ModelSerializer):
    instructor = UserSerializerWithLimitedFields()
    submission = SubmissionSerializerForRead()
    class Meta:
        model = Review
        fields = ('id','instructor','submission','score','review_date','feedback')

class ReviewWriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','instructor','submission','score','review_date','feedback')
        model = Review

    validators = [
        UniqueTogetherValidator(
            queryset=Review.objects.select_related('instructor').all(),
            fields=('instructor','submission'),
            message='You already Reviewd assignment'
        )]
    
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        submission = Submission.objects.get(pk= self.context.get('request').data['submission'])
        # submission = get_object_or_404(Submission,pk= self.context.get('request').data['submission'])
        assignment = Assignment.objects.get(pk=submission.assignment.id)

        if not (assignment.max_score >= validated_data.get('score')):
            raise serializers.ValidationError({'details':f'Max score for given assignment is {assignment.max_score}'})
        

        lesson = Lesson.objects.get(pk=assignment.lesson.id)
        eligibe_instructor =  Course.objects.filter(pk=lesson.course.id,instructor=self.context['request'].data['instructor']).exists()
        if eligibe_instructor:
            # review = Review.objects.create(**validated_data)
            review = Review(**validated_data)
            return review
        else:
            raise serializers.ValidationError({'details':'Instrucator is not valid for given assignment'})
        
from rest_framework import serializers
from .models import Enrollment
from rest_framework.validators import UniqueTogetherValidator
from accounts_app.serializer import UserSerializerWithLimitedFields
from courses_app.serializers import CourseReadSerializers

class EnrollmentReadSerializer(serializers.ModelSerializer):
    student = UserSerializerWithLimitedFields()
    course = CourseReadSerializers()
    class Meta:
        model = Enrollment
        fields = ('id','course','student','enrollment_date','status')

class EnrollmentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('id','student','course','enrollment_date','status')


    validators=[
        UniqueTogetherValidator(
            queryset= Enrollment.objects.select_related('student').all(),
            fields= ['student','course'],
            message= f"student is alredy register whith the given course"
        )
    ]

    # def create(self, validated_data):
    #     print(self.context['request'])
    #     return None
    
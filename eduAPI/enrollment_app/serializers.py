from rest_framework import serializers
from .models import Enrollment
from rest_framework.validators import UniqueTogetherValidator

class EnrollmentSerializer(serializers.ModelSerializer):
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
    #     print()
    #     return super().create(validated_data)
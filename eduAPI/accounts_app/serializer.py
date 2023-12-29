from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','password','role','bio','date_of_birth']
        
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.pop('password'))
        user.save()
        return user
    
    def update(self, instance, validated_data):
        pwd = validated_data.get('password')
        email = validated_data.get('email')
        bio = validated_data.get('bio')
        dob = validated_data.get('date_of_birth')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        if pwd is not None:
            instance.set_password(validated_data.get('password'))
        if email is not None:
            instance.email = email
        if bio is not None:
            instance.bio = bio
        if dob is not None:
            instance.date_of_birth = dob
        if last_name is not None:
            instance.last_name = last_name
        if first_name is not None:
            instance.first_name = first_name

        instance.save()
        return instance
        return super().update(instance, validated_data)
    
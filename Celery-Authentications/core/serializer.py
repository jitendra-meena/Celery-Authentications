from rest_framework import serializers
from django.contrib.auth.models import User
from .models import College

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'username', 'first_name', 'last_name',)

        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user



class SchoolSerializer(serializers.Serializer):
    pass

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
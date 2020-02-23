from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'language', 'price')

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('level', 'prereqs')
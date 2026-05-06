from rest_framework import serializers
from event.models import Course, Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id', 'course', 'title', 'description', 
            'video_url', 'video_file', 'duration_display', 'is_preview'
        ]
        read_only_fields = ['owner']


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'category', 
            'sub_category', 'price', 'image', 'lessons'
        ]
        read_only_fields = ['owner']
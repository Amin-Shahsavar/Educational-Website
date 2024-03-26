from rest_framework import serializers

from apps.bookmark.models import Bookmark
from apps.course.models import Course
from apps.course.serializers import ListCourseSerializer


class BookmarkSerializer(serializers.ModelSerializer):
    course_detail = serializers.SerializerMethodField(read_only=True)

    def get_course_detail(self, obj):
        user = self.context.get('user')
        course_detail = Course.objects.filter(id=obj.course_id)
        serializer = ListCourseSerializer(course_detail, many=True, context={'user': user})
        return serializer.data

    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'course', 'course_detail']
        extra_kwargs = {
            'user': {'read_only': True},
            'course': {'write_only': True},
        }

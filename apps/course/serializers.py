from rest_framework import serializers

from apps.bookmark.models import Bookmark
from apps.course.models import (
    Category,
    Course,
    Video,
    Image,
    Pdf,
)
from apps.plan.models import Plan


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'title_en',
            'video',
            'region',
            'course',
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'title',
            'title_en',
            'image',
            'region',
            'course',
        ]

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = [
            'id',
            'title',
            'title_en',
            'pdf',
            'region',
            'course',
        ]


class SimplePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'title', 'title_en']


class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'title_en']


class ListCourseSerializer(serializers.ModelSerializer):
    plan = SimplePlanSerializer(read_only=True)
    bookmarked = serializers.SerializerMethodField()

    def get_bookmarked(self, obj):
        user = self.context.get('user')
        if user and user.is_authenticated:
            return Bookmark.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'title_en',
            'cover',
            'icon',
            'plan',
            'bookmarked',
        ]


class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    pdfs = PdfSerializer(many=True, read_only=True)
    plan = SimplePlanSerializer(read_only=True)
    category = SimpleCategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'title_en',
            'description',
            'description_en',
            'cover',
            'icon',
            'region',
            'videos',
            'images',
            'pdfs',
            'plan',
            'category',
        ]


class ChildCategorySerializer(serializers.ModelSerializer):
    childrens = serializers.SerializerMethodField()
    courses = serializers.SerializerMethodField()

    def get_childrens(self, obj):
        childrens = Category.objects.filter(parent_category=obj)
        serializer = ChildCategorySerializer(childrens, many=True)
        return serializer.data
    
    def get_courses(self, obj):
        courses = Course.objects.filter(category=obj)
        serializer = ListCourseSerializer(courses, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'title_en',
            'description',
            'description_en',
            'cover',
            'icon',
            'parent_category',
            'childrens',
            'courses',
        ]


class CategorySerializer(serializers.ModelSerializer):
    childrens = ChildCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'title_en',
            'description',
            'description_en',
            'cover',
            'icon',
            'parent_category',
            'childrens',
        ]
        extra_kwargs = {
            'title': {'required': True},
            'title_en': {'required': True},
            'childrens': {'read_only': True},
        }

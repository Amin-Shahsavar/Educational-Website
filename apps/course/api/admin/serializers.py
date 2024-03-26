from rest_framework import serializers

from apps.course.models import (
    Course,
    Video,
    Image,
    Pdf,
    Category,
)
from apps.plan.models import Plan

import ast


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
        extra_kwargs = {
            'video': {'required': True},
            'region': {'required': True},
        }


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
        extra_kwargs = {
            'image': {'required': True},
            'region': {'required': True},
        }


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
        extra_kwargs = {
            'pdf': {'required': True},
            'region': {'required': True},
        }


class SimplePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'title', 'title_en']
        extra_kwargs = {
            'title': {'read_only': True},
            'title_en': {'read_only': True},
        }


class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'title_en']
        extra_kwargs = {
            'title': {'read_only': True},
            'title_en': {'read_only': True},
        }


class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    pdfs = PdfSerializer(many=True, read_only=True)
    plan_detail = serializers.SerializerMethodField()
    category_detail = serializers.SerializerMethodField()

    def get_plan_detail(self, obj):
        plan_detail = Plan.objects.filter(course=obj)
        serializer = SimplePlanSerializer(plan_detail, many=True, read_only=True)
        return serializer.data
    
    def get_category_detail(self, obj):
        category_detail = Category.objects.filter(course=obj)
        serializer = SimpleCategorySerializer(category_detail, many=True, read_only=True)
        return serializer.data

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
            'plan_detail',
            'category',
            'category_detail',
        ]
        extra_kwargs = {
            'title': {'required': True},
            'title_en': {'required': True},
            'description': {'required': True},
            'description_en': {'required': True},
            'plan': {'write_only': True},
            'category': {'write_only': True},
        }
    

class ListCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'title_en',
            'cover',
            'icon',
            'plan',
        ]
        extra_kwargs = {
            'title': {'required': True},
            'title_en': {'required': True},
            'description': {'required': True},
            'description_en': {'required': True},
        }


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


class FlatCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

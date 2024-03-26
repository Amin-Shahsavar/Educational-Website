from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from apps.course.api.admin.serializers import (
    CourseSerializer,
    VideoSerializer,
    ImageSerializer,
    PdfSerializer,
    CategorySerializer,
    FlatCategorySerializer
)
from apps.course.models import (
    Course,
    Video,
    Image,
    Pdf,
    Category,
)
from utils.paginations.page_size import PageSizeNumberPagination
from utils.permissions.superuser import IsSuperUser


class ListCreateCourseView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    pagination_class = PageSizeNumberPagination
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    search_fields = ['title']
    filterset_fields = ['category_id', 'plan', 'region']


class RetrieveUpdateDestroyCourseView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class ListCreateVideoView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    search_fields = ['title']


class RetrieveUpdateDestroyVideoView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class ListCreateImageView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    search_fields = ['title']


class RetrieveUpdateDestroyImageView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ListCreatePdfView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = PdfSerializer
    queryset = Pdf.objects.all()
    search_fields = ['title']


class RetrieveUpdateDestroyPdfView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = PdfSerializer
    queryset = Pdf.objects.all()


class ListCreateCategoryView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = CategorySerializer
    search_fields = ['title']

    def get_queryset(self):
        return Category.objects.filter(parent_category__isnull=True)


class RertieveUpdateDestroyCategoryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ListFlatCategory(generics.ListAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = FlatCategorySerializer
    queryset = Category.objects.all()

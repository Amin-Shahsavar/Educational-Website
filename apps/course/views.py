from django.db.models import Q

from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from apps.course.serializers import (
    ListCourseSerializer,
    CourseSerializer,
    CategorySerializer,
    ChildCategorySerializer,
)
from apps.course.models import (
    Course,
    Category,
)
from utils.paginations.page_size import PageSizeNumberPagination


class ListCourseView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    pagination_class = PageSizeNumberPagination
    serializer_class = ListCourseSerializer
    queryset = Course.objects.all()
    search_fields = ['title', 'title_en']
    filterset_fields = ['category_id']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        else:
            context['user'] = None
        return context


class RetrieveCourseView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.plan:
                return Course.objects.filter(Q(plan=user.plan) | Q(plan__isnull=True)).distinct()
            return Course.objects.filter(plan__isnull=True)
        return Course.objects.filter(plan__isnull=True)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            raise NotFound(detail={"detail": "You don't have any access to this course."})
    

class ListCategoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = CategorySerializer
    search_fields = ['title', 'title_en']

    def get_queryset(self):
        return Category.objects.filter(parent_category__isnull=True)


class RertieveCategoryView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ChildCategorySerializer
    queryset = Category.objects.all()

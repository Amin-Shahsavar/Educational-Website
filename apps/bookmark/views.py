from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.bookmark.models import Bookmark
from apps.bookmark.serializers import BookmarkSerializer
from utils.paginations.page_size import PageSizeNumberPagination


class ListCreateBookmarkView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = BookmarkSerializer
    search_fields = ['course__title', 'course__title_en']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        else:
            context['user'] = None
        return context

    def get_queryset(self):
        return Bookmark.objects.filter(user_id=self.request.user.id)
    
    def create(self, request, *args, **kwargs):
        course_id = request.data.get('course', '')

        if Bookmark.objects.filter(user=self.request.user, course_id=course_id).exists():
            return Response(
                {'message': 'This course is already in your bookmarks.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = BookmarkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data)


class RetrieveDestroyBookmarkView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookmarkSerializer
    lookup_field = 'course_id'

    def get_queryset(self):
        return Bookmark.objects.filter(user_id=self.request.user.id)

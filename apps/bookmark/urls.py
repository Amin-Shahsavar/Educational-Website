from django.urls import path

from apps.bookmark import views


Bookmarks = [
    path(
        'bookmark/',
        views.ListCreateBookmarkView.as_view(),
        name='Bookmark List Create',
    ),
    path(
        'bookmark/<int:course_id>/',
        views.RetrieveDestroyBookmarkView.as_view(),
        name='Bookmark Retrieve Destroy',
    ),
]

urlpatterns = Bookmarks

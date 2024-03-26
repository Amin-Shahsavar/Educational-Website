from django.urls import path

from apps.course import views


Courses = [
    path(
        'course/',
        views.ListCourseView.as_view(),
        name='Courses List',
    ),
    path(
        'course/<int:pk>/',
        views.RetrieveCourseView.as_view(),
        name='Course Retrieve',
    ),
]

Categories = [
    path(
        'category/',
        views.ListCategoryView.as_view(),
        name='Category List',
    ),
    path(
        'category/<int:pk>/',
        views.RertieveCategoryView.as_view(),
        name='Category Retrieve',
    ),
]

urlpatterns = Courses + Categories

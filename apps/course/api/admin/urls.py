from django.urls import path

from apps.course.api.admin import views


Courses = [
    path(
        'course/',
        views.ListCreateCourseView.as_view(),
        name='Courses List Create',
    ),
    path(
        'course/<int:pk>/',
        views.RetrieveUpdateDestroyCourseView.as_view(),
        name='Course Retrieve Update Destroy',
    ),
]

Videos = [
    path(
        'video/',
        views.ListCreateVideoView.as_view(),
        name='Videos List Create',
    ),
    path(
        'video/<int:pk>/',
        views.RetrieveUpdateDestroyVideoView.as_view(),
        name='Video Retrieve Update Destroy',
    ),
]

Images = [
    path(
        'image/',
        views.ListCreateImageView.as_view(),
        name='Images List Create',
    ),
    path('image/<int:pk>/',
         views.RetrieveUpdateDestroyImageView.as_view(),
         name='Image Retrieve Update Destroy',
    ),
]

Pdfs = [
    path(
        'pdf/',
        views.ListCreatePdfView.as_view(),
        name='Pdfs List Create',
    ),
    path(
        'pdf/<int:pk>/',
        views.RetrieveUpdateDestroyPdfView.as_view(),
        name='Pdf Retrieve Update Destroy',
    ),
]

Categories = [
    path(
        'category/',
        views.ListCreateCategoryView.as_view(),
        name='Category List Create',
    ),
    path(
        'category/<int:pk>/',
        views.RertieveUpdateDestroyCategoryView.as_view(),
        name='Category Retrieve Update Destroy',
    ),
    path(
        'flat_category/',
        views.ListFlatCategory.as_view(),
        name='Category Flat List',
    ),
]

urlpatterns = Courses + Videos + Images + Pdfs + Categories

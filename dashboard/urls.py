from django.urls import path

from dashboard import views


urlpatterns = [
    path(
        'dashboard/',
        views.DashboardView.as_view(),
        name='Dashboard Counts',
    ),
]

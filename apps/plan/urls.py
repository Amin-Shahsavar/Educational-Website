from django.urls import path

from apps.plan import views


Plans = [
    path(
        'plan/',
        views.ListPlanView.as_view(),
        name='Plan List',
    ),
    path(
        'plan/<int:pk>/',
        views.RetrievePlanView.as_view(),
        name='Plan Retrieve',
    ),
]

urlpatterns = Plans

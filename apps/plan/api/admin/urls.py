from django.urls import path

from apps.plan.api.admin import views


Plans = [
    path(
        'plan/',
        views.ListCreatePlanView.as_view(),
        name='Plan List Create',
    ),
    path(
        'plan/<int:pk>/',
        views.RetrieveUpdateDestroyPlanView.as_view(),
        name='Plan Retrieve Update Destroy',
    ),
]

urlpatterns = Plans

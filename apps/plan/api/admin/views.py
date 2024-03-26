from rest_framework import generics
from rest_framework.filters import SearchFilter

from apps.plan.api.admin.serializers import PlanSerializer
from apps.plan.models import Plan
from utils.paginations.page_size import PageSizeNumberPagination
from utils.permissions.superuser import IsSuperUser


class ListCreatePlanView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    search_fields = ['title']


class RetrieveUpdateDestroyPlanView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()

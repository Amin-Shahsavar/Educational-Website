from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.plan.models import Plan
from apps.plan.serializers import PlanSerializer
from utils.paginations.page_size import PageSizeNumberPagination


class ListPlanView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    search_fields = ['title', 'title_en']


class RetrievePlanView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()

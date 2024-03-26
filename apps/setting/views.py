from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.setting.models import (
    Service,
    AppVersion,
    ContactUs,
)
from apps.setting.serializers import (
    ServiceSerializer,
    AppVersionSerializer,
    ContactUsSerializer,
)
from utils.paginations.page_size import PageSizeNumberPagination


class ListServiceView(generics.ListAPIView):
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    search_fields = ['title', 'title_en']


class RetrieveServiceView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class CheckAppVersionView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = AppVersionSerializer
    queryset = AppVersion.objects.all()

    def post(self, request, *args, **kwargs):
        app_version = request.data.get('app_version', '')
        last_version = AppVersion.objects.latest('id')
        deprecated_versions = [
                int(av.release_version.replace('.', '')) for av in AppVersion.objects.filter(is_deprecate=True)
            ]
        
        if not app_version:
            return Response(
                {'message': 'app version field is empty.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if int(str(app_version).replace('.', '')) > int(str(last_version).replace('.', '')):
            return Response(
                {'message': 'Version is not valid.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if int(str(app_version).replace('.', '')) < int(str(last_version).replace('.', '')) and not last_version.is_deprecate:
            if int(str(app_version).replace('.', '')) in deprecated_versions:
                return Response(
                    {
                        'message': 'This version is deprecated please update to the last version.',
                        'note': f'The update link is: {last_version}',
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                {
                    'message': 'This is the old version.',
                    'note': f'The last version is {last_version}',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {'message': 'Version check passed.'},
            status=status.HTTP_200_OK,
        )
        

class CreateContactUsView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

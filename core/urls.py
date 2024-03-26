"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'Nikupen Admin'
admin.site.site_title = 'Nikupen Admin'
admin.site.index_title = 'Nikupen'


Admin_API_Rout = [
    path('admin/', admin.site.urls),
    # Users and Plans Admin API
    path('api/admin/', include('apps.user.api.admin.urls'),),
    # Courses, Videos, Images, Pdfs and Categories Admin API
    path('api/admin/', include('apps.course.api.admin.urls')),
    # Plans Admin API
    path('api/admin/', include('apps.plan.api.admin.urls')),
    # DiscountCodes Admin API
    path('api/admin/', include('apps.discount.api.admin.urls')),
    # Payments Admin API
    path('api/admin/', include('apps.payment.api.admin.urls')),
    # Notification Admin API
    path('api/admin/', include('apps.notification.api.admin.urls')),
    # Setting Admin API
    path('api/admin/', include('apps.setting.api.admin.urls')),
    # Dashboard Admin API
    path('api/admin/', include('dashboard.urls')),
]

User_API_Rout = [
    # User Registration API
    path('user/', include('apps.user.urls')),
    # User Notification API
    path('user/', include('apps.notification.urls')),
    # User Bookmark API
    path('user/', include('apps.bookmark.urls')),
    # Course, Videos, Images, Pdfs and Categories User API
    path('', include('apps.course.urls')),
    # Plan User API
    path('', include('apps.plan.urls')),
    # Contact Us User API
    path('setting/', include('apps.setting.urls')),
    # Payment User API
    path('payment/', include('apps.payment.urls')),
]

urlpatterns = Admin_API_Rout + User_API_Rout + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

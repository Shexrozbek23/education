"""agrobase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view
from frontend.views import index

schema_view = get_swagger_view(title='Research Test API', url='/')

urlpatterns = [
    path('api/admin', admin.site.urls),
    path('api/', include(('research.urls', 'research'), namespace="research")),
    # path('api/', include(('users.urls', 'users'), namespace='users')),
    path('api/django_query_profiler', include('django_query_profiler.client.urls')),
    url('api/doc', schema_view),
    re_path(r"^$", index),
    re_path(r"^(?:.*)/?$", index),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#imp for what you want to achieve.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
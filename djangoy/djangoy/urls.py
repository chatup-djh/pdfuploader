"""djangoy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .view import my_api, upload_file, uploadapi
from .view import my_page

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from captcha import urls as captcha_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', my_api, name='my_api'),
    path('page/',my_page,name='my_page'),
    path('upload/', upload_file, name='upload'),
    path('uploadapi/', uploadapi, name='uploadapi'),
    path('api/static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
    path('',include('login.urls')),
    path('captcha/', include(captcha_urls)),
              ] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


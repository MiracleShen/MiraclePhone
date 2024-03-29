"""MiraclePhone URL Configuration

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
from django.urls import path
from django.conf.urls import include, url
from django.contrib.staticfiles.views import serve
import index.views
from django.urls import path, include, re_path


def return_static(request, path, insecure=True, **kwargs):
    return serve(request, path, insecure, **kwargs)


urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    path('admin/', admin.site.urls),
    path('', index.views.index),
    path('news/', index.views.news),
    path('download/', index.views.download),
    path('number/', index.views.number),
    path('customer/', index.views.customer),
    path('park/', index.views.park),
    path('price/', index.views.price),
    path('us/', index.views.us)
]

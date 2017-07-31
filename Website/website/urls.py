"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib import admin
from winapi.views import api_info, dll_info, temp_view, temp_view2


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^winapi/$', TemplateView.as_view(template_name="index.html")),
    url(r'^winapi/api-info/$', api_info, name='api-info'),  # api info
    url(r'^winapi/dll-info/$', dll_info, name='dll-info'),  # dll info
    url(r'^winapi/search/$', temp_view, name='search-info'),  # search
    url(r'^winapi/frequent-dll/$', temp_view2, name='frequent-dll'),  # count frequency
]

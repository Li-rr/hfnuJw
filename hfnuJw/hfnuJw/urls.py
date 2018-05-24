# -*- coding: utf-8 -*-

"""hfnuJw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,handler404,handler500,handler403
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from getLecture import views as getLecture_views
from django.conf import settings
from django.conf.urls.static import static

def prod_static_url():
    '''
    prod 模式下的 url 适配
    '''
    from django.views import static
    urlpattern = url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }, name='static')
    return urlpattern


urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^index/',getLecture_views.index),
    url(r'^login/',getLecture_views.login),
    prod_static_url()
]
urlpatterns += staticfiles_urlpatterns()

handler404 = getLecture_views.page_not_found
handler403 = getLecture_views.permission_denied
handler500 = getLecture_views.page_error

"""quote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from quoteapp.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/',logout_view,name='logout'),
    url(r'^register/',register_view,name='register'),
    url(r'^quote/',quote_view,name='quote'),
    url(r'^all/',allquotes_view,name='allquotes'),
    url(r'^edit/(?P<pk>[0-9]+)/$',edit_view,name='editquotes'),
    url(r'^search/',searchview,name ='searchview'),
    url(r'^delete/(?P<pk>[0-9]+)/$',delete_view,name='deletequotes'),
    url(r'^login',login_view,name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

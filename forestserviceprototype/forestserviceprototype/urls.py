"""forestserviceprototype URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from functools import partial
from django.conf.urls import include, url
from django.contrib import admin
from specialuseform import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^submit/$', views.submit, name="submit"),
    url(r'^submitted/$', views.submitted_permit, name="submitted_permit"),
    url(r'^permit/(?P<permit_id>[0-9]+)/$', views.permit, name="permit"),
    url(r'^applications/', views.applications, name="applications"),
]

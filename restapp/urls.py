# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from restapp import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


#utworzenie routera i zarejestrowanie viewset - ENDpointy utworzone będą automatycznie
router = DefaultRouter()
router.register(r'Get_profile_list', views.ProfileViewSet)
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
]



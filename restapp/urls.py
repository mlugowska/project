from django.conf.urls import url
from restapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^restapp/$', views.profile_list),
    url(r'^restapp/(?P<pk>[0-9]+)/$', views.profile_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
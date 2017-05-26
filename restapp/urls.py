from django.conf.urls import url
from restapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^restapp/$', views.ProfileList.as_view()),
    url(r'^restapp/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
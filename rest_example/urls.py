from django.conf.urls import patterns, url
from django.conf.urls import include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_example.views import (Register, Login, UserList, UserDetail)


urlpatterns = patterns('',
   
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', Register.as_view(), name='register'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
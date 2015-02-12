from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView


urlpatterns = patterns('',
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),name='signup'),
    url(r'^login/$', TemplateView.as_view(template_name="login.html"), name='login'),
       
    url(r'^rest-example/', include('rest_example.urls')),

)

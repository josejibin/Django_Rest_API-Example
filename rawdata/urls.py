from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rawdata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
   
    url(r'^login/$', TemplateView.as_view(template_name="login.html"),
        name='login'),
    

    
    

   
   
    url(r'^rest-auth/', include('rest_example.urls')),
    #url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
  
   
)

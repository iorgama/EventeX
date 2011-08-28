#from django.conf.urls.defaults import patterns, url
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import homepage
from subscription.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'core.views.homepage'),
    
)

#para app subscription
urlpatterns += patterns('subscription.views',
    (r'^inscricao/', 'inscricao' ),
    
)


urlpatterns += staticfiles_urlpatterns()


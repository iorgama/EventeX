from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import homepage 
from subscription.views import inscricao, sucesso
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


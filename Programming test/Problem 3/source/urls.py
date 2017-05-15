from django.conf.urls import include, url
from django.contrib import admin

#urls to the template mapping.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'source.controller.name', name='name'),
    url(r'^home/', 'source.controller.home', name='home'),
    url(r'^tesla/', 'source.controller.tesla', name='tesla'),
]

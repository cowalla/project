from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'graffiti.views.graffiti_index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', 'graffiti.views.api', name='api'),
)

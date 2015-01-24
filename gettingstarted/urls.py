from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import home.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', hello.views.index, name='index'),
    url(r'^api/', include('api.urls')),
    url(r'^db', home.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)

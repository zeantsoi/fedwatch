from django.conf.urls import patterns, include, url

admin.autodiscover()

import api.views

urlpatterns = patterns('',
    url(r'^', include('api.urls')),
    url(r'^db', home.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)

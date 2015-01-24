from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, url, include
from django.views.decorators.cache import cache_page

from api.views import KeywordViewSet


keyword_list = KeywordViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
keyword_detail = KeywordViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    # url(r'^$', api_root),
    url(r'^keywords/$', keyword_list, name='keyword-list'),
    url(r'^keywords/(?P<pk>[0-9]+)/$', keyword_detail, name='keyword-detail'),
])

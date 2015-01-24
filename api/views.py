from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic.base import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.models import Keyword
from api.serializers import KeywordSerializer


class KeywordViewSet(ModelViewSet):
    """ A Custom API View that supports request/response Logging """
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

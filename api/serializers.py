from rest_framework import serializers

from api.models import Keyword


class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = ('id', 'keyword',)

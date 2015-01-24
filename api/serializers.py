from rest_framework import serializers

from api.models import Keyword


class KeywordSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='keyword-detail', format='html')
    
    class Meta:
        model = Keyword
        fields = ('id', 'keyword', 'link',)

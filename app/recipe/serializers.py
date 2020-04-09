from rest_framework import serializers
from core.models import Tag
from django.utils.translation import  ugettext_lazy as _

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id','name')
        read_only_fields = ('id',)
        

from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """Serializer a name field for testing out api view"""
    name=serializers.CharField(max_length=10)
    

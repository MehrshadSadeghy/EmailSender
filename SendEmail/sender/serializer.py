from rest_framework import serializers

from .models import Information


class InformationSerializer(serializers.Serializer):
    """ a serializer for information that the user send """
    to_email = serializers.EmailField(max_length=100)
    subject = serializers.CharField(max_length=255)
    information = serializers.CharField(max_length=1000)

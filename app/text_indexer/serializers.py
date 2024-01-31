"""
Django serializers for handling data serialization and deserialization.
"""
from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    """
    Serializer for handling text data.

    Attributes:
        text (str): A string field for representing text data.
    """

    text = serializers.CharField()


class WordSerializer(serializers.Serializer):
    """
    Serializer for handling word data.

    Attributes:
        word (str): A string field for representing word data.
    """

    word = serializers.CharField()

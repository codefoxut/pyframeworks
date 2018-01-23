from rest_framework import serializers

from rest_api.simple_api.resources import SimpleClass

LANGUAGE_CHOICES = [('hindi', 'HINDI'), ('english', 'ENGLISH'), ('urdu', 'URDU')]

class SimpleSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    country = serializers.CharField(required=False, allow_blank=True, max_length=100)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='urdu')

    def create(self, validated_data):
        """ Create new instance of simpleclass"""
        return SimpleClass(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
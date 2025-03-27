from rest_framework import serializers
from .models import Alert, MediaFile, KnownPerson

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'

class KnownPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnownPerson
        fields = '__all__'

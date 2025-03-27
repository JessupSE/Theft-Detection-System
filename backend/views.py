from rest_framework import viewsets
from .models import Alert, MediaFile, KnownPerson
from .serializers import AlertSerializer, MediaFileSerializer, KnownPersonSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class MediaFileViewSet(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer

class KnownPersonViewSet(viewsets.ModelViewSet):
    queryset = KnownPerson.objects.all()
    serializer_class = KnownPersonSerializer

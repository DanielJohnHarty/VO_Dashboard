from rest_framework import routers, serializers, viewsets
from repo_scanner.models import AudioAsset
from audio_api.serializers import AudioAssetSerializer

# ViewSets define the view behavior.
class AudioAssetViewSet(viewsets.ModelViewSet):
    queryset = AudioAsset.objects.all()
    serializer_class = AudioAssetSerializer
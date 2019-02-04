from rest_framework import serializers
from repo_scanner.models import AudioAsset

# Serializers define the API representation.
class AudioAssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AudioAsset
        fields = ('url', 'filename', 'filepath', 'scandate',
                  'bitrate','length','samplerate','lufs',
                  'channels', 'crc')

from rest_framework import serializers

from apps.base import models

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settings
        fields = ['id','title', 'desc', 'logo', 'email', 'phone']
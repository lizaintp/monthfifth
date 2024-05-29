from rest_framework import serializers

from apps.secondary import models
# from apps.secondary.models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ['id', 'name', 'profession', 'image']
 

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = ['id','question', 'desc']      

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = ['id','title', 'desc', 'image']
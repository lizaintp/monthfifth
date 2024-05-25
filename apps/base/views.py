from django.shortcuts import render
from rest_framework.generics import ListAPIView

from apps.base import models
from apps.base import serializers
# Create your views here.

class SettingsAPIView(ListAPIView):
    queryset = models.Settings.objects.all()
    serializer_class = serializers.SettingsSerializer
    
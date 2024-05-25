from django.shortcuts import render
from rest_framework.generics import ListAPIView

from apps.contacts import models
from apps.contacts import serializers
# Create your views here.

class ContactsAPIView(ListAPIView):
    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer
    
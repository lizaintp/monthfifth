from rest_framework import serializers

from apps.contacts import models

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contacts
        fields = ['id','fullname', 'desc', 'image']
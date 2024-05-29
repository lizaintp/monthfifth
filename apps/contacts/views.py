from rest_framework.generics import (ListAPIView, CreateAPIView,
                                      UpdateAPIView, DestroyAPIView, RetrieveAPIView)

from apps.contacts import models
from apps.contacts import serializers
# Create your views here.

# class ContactsAPIView(ListAPIView):
#     queryset = models.Contacts.objects.all()
#     serializer_class = serializers.ContactsSerializer
    
class ContactsListAPIView(ListAPIView):
    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer

class ContactsCreateAPIView(CreateAPIView):
    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer

class ContactsUpdateAPIView(UpdateAPIView):
    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer

class ContactsDestroyAPIView(DestroyAPIView):
    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer

class ContactsRetrieveAPIView(RetrieveAPIView):
    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer
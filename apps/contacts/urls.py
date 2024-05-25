from django.urls import path
from apps.contacts import views

urlpatterns = [
    path('', views.ContactsAPIView.as_view(), name='api_contacts')
]
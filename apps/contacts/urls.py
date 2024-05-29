from django.urls import path
from apps.contacts import views

urlpatterns = [
    # path('', views.ContactsAPIView.as_view(), name='api_contacts'),
    path('contacts/', views.ContactsListAPIView.as_view(), name='api_contacts'),
    path('contacts/create', views.ContactsCreateAPIView.as_view(), name='api_contacts'),
    path('contacts/update', views.ContactsUpdateAPIView.as_view(), name='api_contacts'),
    path('contacts/destroy', views.ContactsDestroyAPIView.as_view(), name='api_contacts'),
    path('contacts/retrieve', views.ContactsRetrieveAPIView.as_view(), name='api_contacts'),
]
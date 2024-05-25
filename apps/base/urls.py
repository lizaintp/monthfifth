from django.urls import path
from apps.base import views

urlpatterns = [
    path('', views.SettingsAPIView.as_view(), name='api_settings')
]
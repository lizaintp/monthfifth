from django.urls import path
from apps.secondary import views

urlpatterns = [
    # Team
    path('team/', views.TeamListAPIView.as_view(), name='api_team'),
    path('team/create', views.TeamCreateAPIView.as_view(), name='api_team_create'),
    path('team/update', views.TeamUpdateAPIView.as_view(), name='api_team_update'),
    path('team/destroy', views.TeamDestroyAPIView.as_view(), name='api_team_destroy'),
    path('team/<int:pk>/', views.TeamRetrieveAPIView.as_view(), name='api_team_retrieve'),

    # FAQ
    path('faq/', views.FAQListAPIView.as_view(), name='api_faq'),
    path('faq/create', views.FAQCreateAPIView.as_view(), name='api_faq_create'),
    path('faq/update', views.FAQUpdateAPIView.as_view(), name='api_faq_update'),
    path('faq/destroy', views.FAQDestroyAPIView.as_view(), name='api_faq_destroy'),
    path('faq/<int:pk>/', views.FAQRetrieveAPIView.as_view(), name='api_faq_retrieve'),

    # Service
    path('service/', views.ServiceListAPIView.as_view(), name='api_service'),
    path('service/create', views.ServiceCreateAPIView.as_view(), name='api_service_create'),
    path('service/update', views.ServiceUpdateAPIView.as_view(), name='api_service_update'),
    path('service/destroy', views.ServiceDestroyAPIView.as_view(), name='api_service_destroy'),
    path('service/<int:pk>/', views.ServiceRetrieveAPIView.as_view(), name='api_service_retrieve'),


]

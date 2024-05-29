from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from apps.secondary import models
from apps.secondary import serializers

# Team
class TeamListAPIView(ListAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class TeamCreateAPIView(CreateAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class TeamUpdateAPIView(UpdateAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class TeamDestroyAPIView(DestroyAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class TeamRetrieveAPIView(RetrieveAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

# FAQ

class FAQListAPIView(ListAPIView):
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerializer

class FAQCreateAPIView(CreateAPIView):
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerializer

class FAQUpdateAPIView(UpdateAPIView):
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerializer

class FAQDestroyAPIView(DestroyAPIView):
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerializer

class FAQRetrieveAPIView(RetrieveAPIView):
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerializer

# Service

class ServiceListAPIView(ListAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

class ServiceCreateAPIView(CreateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

class ServiceUpdateAPIView(UpdateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

class ServiceDestroyAPIView(DestroyAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

class ServiceRetrieveAPIView(RetrieveAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


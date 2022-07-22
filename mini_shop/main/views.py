from rest_framework import viewsets

from .serializers import OrganizationSerializer, ShopSerializer
from .models import Organization, Shop


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

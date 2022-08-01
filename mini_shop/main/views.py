from django.http import HttpResponse
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from .serializers import OrganizationSerializer, ShopSerializer
from .models import Organization, Shop
from django.core.mail import send_mail

import csv


class ShopViewSet(mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def update(self, request, *args, **kwargs):
        """Updates existing shop"""
        return super().update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """Get the list of all shops"""
        return super().list(request, *args, **kwargs)


class OrganizationViewSet(mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    @action(methods=['get'], detail=True)
    def shops_file(self, request, pk):
        """Returns csv-file of all shops related to the organization as a response"""
        shops = [ShopSerializer(n).data for n in Shop.objects.filter(organization=int(pk))]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="shops_{pk}.csv"'
        writer = csv.writer(response)
        writer.writerow(shops[0].keys())
        for obj in shops:
            writer.writerow(
                [i for i in obj.values()])
        return response

    def update(self, request, *args, **kwargs):
        """Updates existing organization"""
        return super().update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """Get the list of all organizations"""
        return super().list(request, *args, **kwargs)

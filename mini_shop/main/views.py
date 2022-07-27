from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import OrganizationSerializer, ShopSerializer
from .models import Organization, Shop

import csv


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    @action(methods=['get'], detail=True)
    def shops_file(self, request, pk):
        """Returns csv-file of all shops related to the organization as a response"""
        shops = [ShopSerializer(n).data for n in Shop.objects.all() if n.organization.id == int(pk)]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="shops_{pk}.csv"'
        writer = csv.writer(response)
        writer.writerow(shops[0].keys())
        for obj in shops:
            writer.writerow(
                [i for i in obj.values()])
        return response

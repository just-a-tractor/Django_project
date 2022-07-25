from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import OrganizationSerializer, ShopSerializer
from .models import Organization, Shop

import pandas as pd


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    @action(methods=['get'], detail=True)
    def shops_file(self, request, pk):
        shops = Shop.objects.all()
        file_path = "main/files/shops.xlsx"
        form_xlsx([ShopSerializer(n).data for n in shops if n.organization_id.id == int(pk)], file_path)
        # TODO: do something with organization_id.id
        return return_xlsx(file_path)


def form_xlsx(data=None, file_path=""):
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter(file_path, engine='openpyxl')
    df.to_excel(writer, index=False)
    writer.save()


def return_xlsx(file_path=None):
    with open("./" + file_path, 'rb') as f:
        file_data = f.read()
    response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{file_path.split("/")[-1]}"'
    return response

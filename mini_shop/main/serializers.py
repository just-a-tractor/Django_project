from rest_framework import serializers
from .models import *


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'description', 'address', 'index', 'is_deleted', 'organization_id')


class OrganizationSerializer(serializers.ModelSerializer):
    # shops = ShopSerializer(many=True)

    class Meta:
        model = Organization
        fields = ('name', 'description')

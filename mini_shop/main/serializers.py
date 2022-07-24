from rest_framework import serializers
from .models import Organization, Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'name', 'description', 'organization_id', 'address', 'index')
        # TODO: return only if not is_deleted
        # TODO: find a way to remove organization_id without POST break


class OrganizationSerializer(serializers.ModelSerializer):
    shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'shops')

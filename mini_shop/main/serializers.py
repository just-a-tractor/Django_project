from rest_framework import serializers
from .models import Organization, Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'name', 'description', 'address', 'index', 'is_deleted')


class OrganizationSerializer(serializers.ModelSerializer):
    shops = serializers.SerializerMethodField()

    def get_shops(self, obj):
        qs = Shop.objects.filter(organization=obj, is_deleted=False)
        serialized = ShopSerializer(qs, many=True)
        return serialized.data

    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'shops')

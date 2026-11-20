from rest_framework import serializers
from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(
        source="business.name",
        read_only=True,
    )

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "business",
            "business_name",
            "name",
            "description",
            "category",
            "price",
            "image",
            "is_available",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "business",
            "business_name",
            "created_at",
            "updated_at",
        ]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")

        return value

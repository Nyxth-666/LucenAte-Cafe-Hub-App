from rest_framework import serializers

from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(
        source="business.name",
        read_only=True,
    )

    business_type = serializers.CharField(
        source="business.business_type",
        read_only=True,
    )

    price_range = serializers.CharField(
        source="business.price_range",
        read_only=True,
    )

    class Meta:
        model = Favorite
        fields = [
            "id",
            "business",
            "business_name",
            "business_type",
            "price_range",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

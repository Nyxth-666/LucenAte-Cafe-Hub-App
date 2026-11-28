from rest_framework import serializers

from apps.businesses.models import Business, BusinessOperatingHours
from apps.locations.models import BusinessLocation


class BusinessLocationDiscoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessLocation
        fields = [
            "street_address",
            "barangay",
            "city",
            "province",
            "latitude",
            "longitude",
        ]


class BusinessOperatingHoursDiscoverySerializer(serializers.ModelSerializer):
    day_name = serializers.CharField(
        source="get_day_display",
        read_only=True,
    )

    class Meta:
        model = BusinessOperatingHours
        fields = [
            "day",
            "day_name",
            "opening",
            "closing",
            "is_closed",
        ]


class BusinessDiscoverySerializer(serializers.ModelSerializer):
    locations = BusinessLocationDiscoverySerializer(
        many=True,
        read_only=True,
    )

    features = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )

    class Meta:
        model = Business
        fields = [
            "id",
            "name",
            "business_type",
            "price_range",
            "phone_number",
            "email",
            "description",
            "features",
            "locations",
            "created_at",
        ]


class BusinessDetailSerializer(serializers.ModelSerializer):
    locations = BusinessLocationDiscoverySerializer(
        many=True,
        read_only=True,
    )

    features = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )

    operating_hours = BusinessOperatingHoursDiscoverySerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Business
        fields = [
            "id",
            "name",
            "business_type",
            "price_range",
            "phone_number",
            "email",
            "description",
            "features",
            "locations",
            "operating_hours",
            "created_at",
        ]


class BusinessDiscoverySerializer(serializers.ModelSerializer):
    review_count = serializers.IntegerField(read_only=True)

    locations = BusinessLocationDiscoverySerializer(
        many=True,
        read_only=True,
    )

    features = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )

    class Meta:
        model = Business
        fields = [
            "id",
            "name",
            "business_type",
            "price_range",
            "phone_number",
            "email",
            "description",
            "features",
            "locations",
            "created_at",
            "review_count",
        ]

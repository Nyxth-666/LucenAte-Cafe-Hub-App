from rest_framework import serializers
from .models import BusinessLocation

class BusinessLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessLocation
        fields = [
            "id",
            "street_address",
            "barangay",
            "city",
            "province",
            "latitude",
            "longitude",
        ]
        read_only_fields = ["id"]

    def validate(self, attrs):
        latitude = attrs.get("latitude")
        longitude = attrs.get("longitude")

        if (latitude is None) != (longitude is None):
            raise serializers.ValidationError(
                "Latitude and longitude must both be provided."
            )

        if latitude is not None and not -90 <= latitude <= 90:
            raise serializers.ValidationError(
                "Latitude must be between -90 and 90."
            )

        if longitude is not None and not -180 <= longitude <= 180:
            raise serializers.ValidationError(
                "Longitude must be between -180 and 180."
            )

        return attrs

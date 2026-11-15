from rest_framework import serializers
from .models import (
    Business,
    BusinessFeature,
    BusinessOperatingHours,
    BusinessDocument,
)

class BusinessOperatingHoursSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessOperatingHours
        fields = [
            "day",
            "opening",
            "closing",
            "is_closed",
        ]

    def validate(self, attrs):
        is_closed = attrs.get("is_closed", False)
        opening = attrs.get("opening")
        closing = attrs.get("closing")

        if not is_closed:
            if not opening or not closing:
                raise serializers.ValidationError(
                    "Opening and closing times are required for open days."
                )

            if opening >= closing:
                raise serializers.ValidationError(
                    "Closing time must be later than opening time."
                )

        return attrs

class BusinessSerializer(serializers.ModelSerializer):

    features = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=BusinessFeature.objects.all(),
        required=False,
    )

    operating_hours = BusinessOperatingHoursSerializer(
        many=True,
        required=False,
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
            "operating_hours",
            "status",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "status",
            "created_at",
        ]

    def validate_operating_hours(self, value):
        days = [item["day"] for item in value]

        if len(days) != len(set(days)):
            raise serializers.ValidationError(
                "Each day can only have one operating-hours entry."
            )

        return value

    def create(self, validated_data):
        operating_hours_data = validated_data.pop(
            "operating_hours", []
        )

        features_data = validated_data.pop("features", [])

        business = Business.objects.create(**validated_data)

        business.features.set(features_data)

        for hours in operating_hours_data:
            BusinessOperatingHours.objects.create(
                business=business,
                **hours,
            )

        return business

class BusinessDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessDocument
        fields = [
            "id",
            "document",
            "uploaded_at",
        ]
        read_only_fields = [
            "id",
            "uploaded_at",
        ]

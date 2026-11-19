from rest_framework import serializers
from .models import (
    Business,
    BusinessFeature,
    BusinessOperatingHours,
    BusinessDocument,
)
from apps.locations.serializers import BusinessLocationSerializer


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
        operating_hours_data = validated_data.pop("operating_hours", [])

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


class BusinessDocumentReviewSerializer(serializers.ModelSerializer):
    filename = serializers.SerializerMethodField()

    class Meta:
        model = BusinessDocument
        fields = [
            "id",
            "filename",
            "uploaded_at",
        ]

    def get_filename(self, obj):
        return obj.document.name.split("/")[-1]


class BusinessReviewSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()
    owner_email = serializers.EmailField(
        source="owner.email",
        read_only=True,
    )

    features = serializers.StringRelatedField(many=True)

    locations = BusinessLocationSerializer(many=True, read_only=True)

    operating_hours = BusinessOperatingHoursSerializer(
        many=True,
        read_only=True,
    )

    documents = BusinessDocumentReviewSerializer(
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
            "status",
            "owner_name",
            "owner_email",
            "features",
            "locations",
            "operating_hours",
            "documents",
            "created_at",
        ]

    def get_owner_name(self, obj):
        return obj.owner.get_full_name() or obj.owner.username


class BusinessOwnerReviewSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()


class BusinessLocationReviewSerializer(serializers.ModelSerializer):
    class Meta:
        from apps.locations.models import BusinessLocation

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


class BusinessDocumentReviewSerializer(serializers.ModelSerializer):
    document_name = serializers.SerializerMethodField()

    class Meta:
        model = BusinessDocument
        fields = [
            "id",
            "document_name",
            "uploaded_at",
        ]

    def get_document_name(self, obj):
        return obj.document.name.split("/")[-1]


class BusinessApplicationReviewSerializer(serializers.ModelSerializer):
    owner = BusinessOwnerReviewSerializer(read_only=True)
    locations = BusinessLocationReviewSerializer(many=True, read_only=True)
    operating_hours = BusinessOperatingHoursSerializer(
        many=True,
        read_only=True,
    )
    documents = BusinessDocumentReviewSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Business
        fields = [
            "id",
            "owner",
            "name",
            "business_type",
            "price_range",
            "phone_number",
            "email",
            "description",
            "features",
            "locations",
            "operating_hours",
            "documents",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["owner"] = {
            "first_name": instance.owner.first_name,
            "last_name": instance.owner.last_name,
            "email": instance.owner.email,
        }

        data["features"] = list(instance.features.values_list("name", flat=True))

        return data

from rest_framework import serializers
from .models import Visit


class VisitSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(
        source="business.name",
        read_only=True,
    )

    class Meta:
        model = Visit
        fields = [
            "id",
            "user",
            "business",
            "business_name",
            "note",
            "visited_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "business",
            "business_name",
            "visited_at",
        ]

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.text import slugify
from rest_framework import serializers
from uuid import uuid4

from django.db import transaction
from apps.businesses.serializers import BusinessSerializer
from apps.locations.serializers import BusinessLocationSerializer

User = get_user_model()


class BusinessOwnerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
    )

    business = BusinessSerializer(write_only=True)
    location = BusinessLocationSerializer(write_only=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "business",
            "location",
        ]

    def validate_email(self, value):
        email = value.strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                "An account with this email already exists."
            )

        return email

    @transaction.atomic
    def create(self, validated_data):
        business_data = validated_data.pop("business")
        location_data = validated_data.pop("location")

        email = validated_data["email"]

        username_base = slugify(email.split("@")[0])[:130] or "user"
        username = f"{username_base}_{uuid4().hex[:8]}"

        user = User.objects.create_user(
            username=username,
            email=email,
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            role=User.Role.BUSINESS_OWNER,
        )

        business = BusinessSerializer().create(
            {
                **business_data,
                "owner": user,
            }
        )

        location_data["business"] = business
        location = BusinessLocationSerializer().create(location_data)

        return user


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
        ]

    def validate_email(self, value):
        email = value.strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                "An account with this email already exists."
            )

        return email

    def create(self, validated_data):
        email = validated_data["email"]

        username_base = slugify(email.split("@")[0])[:130] or "user"
        username = f"{username_base}_{uuid4().hex[:8]}"

        user = User.objects.create_user(
            username=username,
            email=email,
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            role=User.Role.USER,
        )

        return user

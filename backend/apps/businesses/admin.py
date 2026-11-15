from django.contrib import admin
from .models import (
    Business,
    BusinessDocument,
    BusinessFeature,
    BusinessOperatingHours,
)

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "owner",
        "business_type",
        "price_range",
        "phone_number",
        "email",
        "status",
        "display_features",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "owner__username",
        "owner__email",
    )

    list_filter = (
        "business_type",
        "price_range",
        "status",
    )

    @admin.display(description="Features")
    def display_features(self, obj):
        return ", ".join(
            feature.name for feature in obj.features.all()
        )


@admin.register(BusinessDocument)
class BusinessDocumentAdmin(admin.ModelAdmin):

    list_display = (
        "business",
        "document",
        "uploaded_at",
    )

    search_fields = (
        "business__name",
    )

@admin.register(BusinessFeature)
class BusinessFeatureAdmin(admin.ModelAdmin):

    list_display = ("name",)

    search_fields = ("name",)

    ordering = ("name",)

@admin.register(BusinessOperatingHours)
class BusinessOperatingHoursAdmin(admin.ModelAdmin):

    list_display = (
        "business",
        "day",
        "opening",
        "closing",
        "is_closed",
    )

    search_fields = (
        "business__name",
    )

    list_filter = (
        "day",
        "is_closed",
    )

    ordering = (
        "business",
        "day",
    )

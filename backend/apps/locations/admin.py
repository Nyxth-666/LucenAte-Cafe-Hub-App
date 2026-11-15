from django.contrib import admin
from .models import BusinessLocation

@admin.register(BusinessLocation)
class BusinessLocationAdmin(admin.ModelAdmin):

    list_display = (
        "business",
        "street_address",
        "barangay",
        "city",
        "province",
        "latitude",
        "longitude",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "business__name",
        "street_address",
        "barangay",
        "city",
    )

    list_filter = (
        "city",
        "province",
    )

    ordering = (
        "business",
        "city",
    )

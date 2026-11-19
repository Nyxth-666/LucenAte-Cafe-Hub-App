from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.businesses.models import Business
from .serializers import (
    BusinessDiscoverySerializer,
    BusinessDetailSerializer,
)


class BusinessDiscoveryView(generics.ListAPIView):
    serializer_class = BusinessDiscoverySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = (
            Business.objects.filter(status=Business.Status.APPROVED)
            .prefetch_related(
                "features",
                "locations",
            )
            .order_by("name")
        )

        search = self.request.query_params.get("search")
        business_type = self.request.query_params.get("business_type")
        price_range = self.request.query_params.get("price_range")
        barangay = self.request.query_params.get("barangay")

        if search:
            queryset = queryset.filter(name__icontains=search)

        if business_type:
            queryset = queryset.filter(business_type=business_type.upper())

        if price_range:
            queryset = queryset.filter(price_range=price_range)

        if barangay:
            queryset = queryset.filter(locations__barangay__icontains=barangay)

        return queryset.distinct()

class BusinessDetailView(generics.RetrieveAPIView):
    serializer_class = BusinessDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return (
            Business.objects
            .filter(status=Business.Status.APPROVED)
            .prefetch_related(
                "features",
                "locations",
                "operating_hours",
            )
        )

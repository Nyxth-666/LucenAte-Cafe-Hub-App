from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.businesses.models import Business
from .serializers import (
    BusinessDiscoverySerializer,
    BusinessDetailSerializer,
)

from django.db.models import Count


class BusinessDiscoveryView(generics.ListAPIView):
    serializer_class = BusinessDiscoverySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = (
            Business.objects.filter(status=Business.Status.APPROVED)
            .annotate(review_count=Count("reviews", distinct=True))
            .prefetch_related(
                "features",
                "locations",
            )
        )

        search = self.request.query_params.get("search")
        business_type = self.request.query_params.get("business_type")
        price_range = self.request.query_params.get("price_range")
        barangay = self.request.query_params.get("barangay")
        hidden_gems = self.request.query_params.get("hidden_gems")

        if search:
            queryset = queryset.filter(name__icontains=search)

        if business_type:
            queryset = queryset.filter(business_type=business_type.upper())

        if price_range:
            queryset = queryset.filter(price_range=price_range)

        if barangay:
            queryset = queryset.filter(
                locations__barangay__icontains=barangay
            )

        if hidden_gems == "true":
            queryset = (
                queryset
                .filter(review_count__lte=5)
                .order_by("review_count", "-created_at")
            )
        else:
            queryset = queryset.order_by("name")

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

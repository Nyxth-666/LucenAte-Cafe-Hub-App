from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.accounts.permissions import IsAdministrator
from .models import Business, BusinessDocument
from .serializers import BusinessDocumentSerializer, BusinessApplicationReviewSerializer


class BusinessDocumentUploadView(generics.CreateAPIView):
    serializer_class = BusinessDocumentSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        business = get_object_or_404(
            Business,
            id=self.kwargs["business_id"],
            owner=self.request.user,
        )

        serializer.save(business=business)


class PendingBusinessApplicationsView(generics.ListAPIView):
    serializer_class = BusinessApplicationReviewSerializer
    permission_classes = [IsAdministrator]

    def get_queryset(self):
        return (
            Business.objects.filter(status=Business.Status.PENDING)
            .select_related("owner")
            .prefetch_related(
                "features",
                "locations",
                "operating_hours",
                "documents",
            )
            .order_by("created_at")
        )


class ApproveBusinessApplicationView(APIView):
    permission_classes = [IsAdministrator]

    def post(self, request, business_id):
        business = get_object_or_404(
            Business,
            id=business_id,
        )

        if business.status != Business.Status.PENDING:
            return Response(
                {"detail": "Only pending applications can be approved."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        business.status = Business.Status.APPROVED
        business.save(update_fields=["status", "updated_at"])

        return Response(
            {
                "detail": "Business application approved successfully.",
                "business_id": business.id,
                "status": business.status,
            },
            status=status.HTTP_200_OK,
        )


class RejectBusinessApplicationView(APIView):
    permission_classes = [IsAdministrator]

    def post(self, request, business_id):
        business = get_object_or_404(
            Business,
            id=business_id,
        )

        if business.status != Business.Status.PENDING:
            return Response(
                {"detail": "Only pending applications can be rejected."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        business.status = Business.Status.REJECTED
        business.save(update_fields=["status", "updated_at"])

        return Response(
            {
                "detail": "Business application rejected successfully.",
                "business_id": business.id,
                "status": business.status,
            },
            status=status.HTTP_200_OK,
        )

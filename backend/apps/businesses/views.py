from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Business, BusinessDocument
from .serializers import BusinessDocumentSerializer

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

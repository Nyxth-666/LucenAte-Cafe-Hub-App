from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.businesses.models import Business
from .models import Visit
from .serializers import VisitSerializer


class VisitListView(generics.ListAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Visit.objects.filter(user=self.request.user).select_related("business")


class VisitCreateView(generics.CreateAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        business = get_object_or_404(
            Business,
            id=self.kwargs["business_id"],
            status=Business.Status.APPROVED,
        )

        serializer.save(
            user=self.request.user,
            business=business,
        )


class VisitDeleteView(generics.DestroyAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Visit.objects.filter(user=self.request.user)

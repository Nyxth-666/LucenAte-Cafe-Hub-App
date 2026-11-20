from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from apps.businesses.models import Business
from .models import MenuItem
from .serializers import MenuItemSerializer


class BusinessMenuListCreateView(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return MenuItem.objects.filter(
            business_id=self.kwargs["business_id"],
            business__status=Business.Status.APPROVED,
        ).select_related("business")

    def perform_create(self, serializer):
        business = get_object_or_404(
            Business,
            id=self.kwargs["business_id"],
            owner=self.request.user,
        )

        serializer.save(business=business)


class MenuItemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MenuItem.objects.filter(
            business__owner=self.request.user
        ).select_related("business")

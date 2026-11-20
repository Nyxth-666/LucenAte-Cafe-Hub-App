from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer


class BusinessReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return (
            Review.objects
            .filter(
                business_id=self.kwargs["business_id"],
                business__status="APPROVED",
            )
            .select_related("user")
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            business_id=self.kwargs["business_id"],
        )


class ReviewUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

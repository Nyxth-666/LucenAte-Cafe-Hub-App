from django.urls import path

from .views import (
    BusinessReviewListCreateView,
    ReviewUpdateDeleteView,
)

urlpatterns = [
    path(
        "businesses/<int:business_id>/",
        BusinessReviewListCreateView.as_view(),
        name="business-reviews",
    ),
    path(
        "<int:pk>/",
        ReviewUpdateDeleteView.as_view(),
        name="review-detail",
    ),
]

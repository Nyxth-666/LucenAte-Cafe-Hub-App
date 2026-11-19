from django.urls import path

from .views import BusinessDiscoveryView, BusinessDetailView

urlpatterns = [
    path(
        "businesses/",
        BusinessDiscoveryView.as_view(),
        name="business-discovery",
    ),
    path(
        "businesses/<int:pk>/",
        BusinessDetailView.as_view(),
        name="business-detail",
    ),
]

from django.urls import path

from .views import (
    BusinessMenuListCreateView,
    MenuItemUpdateDeleteView,
)

urlpatterns = [
    path(
        "businesses/<int:business_id>/",
        BusinessMenuListCreateView.as_view(),
        name="business-menu",
    ),
    path(
        "<int:pk>/",
        MenuItemUpdateDeleteView.as_view(),
        name="menu-item-detail",
    ),
]

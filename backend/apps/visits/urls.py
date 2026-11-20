from django.urls import path

from .views import (
    VisitListView,
    VisitCreateView,
    VisitDeleteView,
)

urlpatterns = [
    path(
        "",
        VisitListView.as_view(),
        name="visit-list",
    ),
    path(
        "businesses/<int:business_id>/check-in/",
        VisitCreateView.as_view(),
        name="visit-create",
    ),
    path(
        "<int:pk>/",
        VisitDeleteView.as_view(),
        name="visit-delete",
    ),
]

from django.urls import path
from .views import (
    BusinessDocumentUploadView,
    PendingBusinessApplicationsView,
    ApproveBusinessApplicationView,
    RejectBusinessApplicationView,
)

urlpatterns = [
    path(
        "<int:business_id>/documents/upload/",
        BusinessDocumentUploadView.as_view(),
        name="business-document-upload",
    ),
    path(
        "applications/pending/",
        PendingBusinessApplicationsView.as_view(),
        name="pending-business-applications",
    ),
    path(
    "<int:business_id>/approve/",
    ApproveBusinessApplicationView.as_view(),
    name="approve-business-application",
    ),
    path(
        "<int:business_id>/reject/",
        RejectBusinessApplicationView.as_view(),
        name="reject-business-application",
    ),
]

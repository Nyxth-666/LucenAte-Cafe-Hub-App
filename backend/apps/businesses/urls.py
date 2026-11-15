from django.urls import path
from .views import BusinessDocumentUploadView

urlpatterns = [
    path(
        "<int:business_id>/documents/upload/",
        BusinessDocumentUploadView.as_view(),
        name="business-document-upload",
    ),
]

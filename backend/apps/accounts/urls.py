from django.urls import path
from . views import BusinessOwnerRegistrationView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(
        "register/business-owner/",
        BusinessOwnerRegistrationView.as_view(),
        name="business-owner-register",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

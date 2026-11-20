from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/accounts/",
        include("apps.accounts.urls"),
    ),

    path(
        "api/businesses/",
        include("apps.businesses.urls"),
    ),

    path(
        "api/discovery/",
        include("apps.discovery.urls")
    ),

    path(
        "api/favorites/",
        include("apps.favorites.urls")
    ),

    path(
        "api/reviews/",
        include("apps.reviews.urls")
    ),

    path(
        "api/menus/",
        include("apps.menus.urls")
    ),

    path(
        "api/visits/",
        include("apps.visits.urls")
    ),
]

"""
URL configuration for app project.
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Admin Interface
    path("admin/", admin.site.urls),
    # API Schema Generation
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    # Swagger Documentation
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    # User-related API Endpoints
    path("api/user/", include("user.urls")),
    # Text Indexer API Endpoints
    path("api/", include("text_indexer.urls")),
]

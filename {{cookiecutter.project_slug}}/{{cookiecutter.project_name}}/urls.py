from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("auth/token-refresh/", refresh_jwt_token),
]

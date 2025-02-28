from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("user.urls")),
    path("", include("system.urls")),
]
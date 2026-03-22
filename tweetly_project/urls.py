from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.shortcuts import redirect
from django.views.static import serve

urlpatterns = [
    path("", lambda request: redirect("/tweets/")),
    path("tweets/", include("tweets.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

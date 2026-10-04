from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        account_views.dashboard,
        name="dashboard"
    ),

    path(
        "stations/",
        include("stations.urls")
    ),

    path(
        "bookings/",
        include("bookings.urls")
    ),

    path(
        "vehicles/",
        include("vehicles.urls")
    ),

    path(
        "payments/",
        include("payments.urls")
    ),

    path(
        "notifications/",
        include("user_notifications.urls")
    ),

    path(
        "account/",
        include("accounts.urls")
    ),
    path(
    "ai/",
    include("ai_assistant.urls")
    ),
    path(
    "charging/",
    include("charging.urls")
    ),
]


# =========================================================
# MEDIA FILES
# Profile images / uploaded files
# =========================================================

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
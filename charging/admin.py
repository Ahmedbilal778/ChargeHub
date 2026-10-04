from django.contrib import admin
from .models import ChargingSession


@admin.register(ChargingSession)
class ChargingSessionAdmin(admin.ModelAdmin):
    list_display = (
        "booking",
        "status",
        "start_time",
        "end_time",
        "energy_consumed",
        "charging_cost",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "booking__booking_id",
        "booking__user__username",
    )
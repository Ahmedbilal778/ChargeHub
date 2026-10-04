from django.contrib import admin
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "vehicle_name",
        "vehicle_number",
        "owner",
        "vehicle_type",
        "current_battery",
        "range_km",
    )

    list_filter = (
        "vehicle_type",
    )

    search_fields = (
        "vehicle_name",
        "vehicle_number",
        "owner__username",
    )